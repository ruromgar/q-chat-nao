from django.contrib.auth.models import User
from activities.models import Activity01, Activity02, Activity03, Activity04, Activity05, Activity06
from autismws.models import UserProfile

import pandas as pd
from sklearn.externals import joblib

from content.models.train import build_model

import logging

logger = logging.getLogger(__name__)


def get_user_data(pk):
    user = User.objects.get(pk=pk)
    user_profile = UserProfile.objects.get(user_id=user.id)

    a01 = binarize_answer(Activity01.objects.filter(patient_id=user.id).first())
    a02 = binarize_answer(Activity02.objects.filter(patient_id=user.id).first())
    a03 = binarize_answer(Activity03.objects.filter(patient_id=user.id).first())
    a04 = binarize_answer(Activity04.objects.filter(patient_id=user.id).first())
    a05 = binarize_answer(Activity05.objects.filter(patient_id=user.id).first())
    a06 = binarize_answer(Activity06.objects.filter(patient_id=user.id).first())
    ai01 = binarize_info(1, user_profile.q_ai_1)
    ai02 = binarize_info(2, user_profile.q_ai_2)
    ai03 = binarize_info(3, user_profile.q_ai_3)
    ai04 = binarize_info(4, user_profile.q_ai_4)
    age = user_profile.age
    gender = 0 if user_profile.gender == 'F' else 1
    tea = user_profile.tea
    added_to_dataset = user_profile.added_to_dataset

    data = {
        "Actividad 1": a01,
        "Actividad 2": a02,
        "Actividad 3": a03,
        "Actividad 4": a04,
        "Actividad 5": a05,
        "Actividad 6": a06,
        "Información previa 1": ai01,
        "Información previa 2": ai02,
        "Información previa 3": ai03,
        "Información previa 4": ai04,
        "Edad": age,
        "Género": gender,
        "TEA": tea,
        "Guardado": added_to_dataset
    }

    return data


def get_user_prediction(pk):

    answers = get_user_data(pk)

    # Removing unneeded data
    answers.pop('Guardado', None)

    if answers["TEA"] is not None:
        answers["RESULTADO FINAL"] = \
            "El usuario presenta rasgos característicos de TEA. Se sugiere realizar un análisis en profundidad." \
            if answers["TEA"] else "El usuario no parece tener rasgos de TEA."
    else:

        is_user_done = True
        for k, v in answers.values():
            if v is None:
                is_user_done = False
                answers[k] = '-'

        if not is_user_done:
            answers["RESULTADO FINAL"] = "No hay datos suficientes para valorar a este usuario."
        else:
            user_data = [[
                answers["Actividad 1"],
                answers["Actividad 2"],
                answers["Actividad 3"],
                answers["Actividad 4"],
                answers["Actividad 5"],
                answers["Actividad 6"],
                answers["Información previa 1"],
                answers["Información previa 2"],
                answers["Información previa 3"],
                answers["Información previa 4"],
                answers["Edad"],
                answers["Género"]
            ]]
            answers["RESULTADO FINAL"] = predict_user(user_data, pk)

    return answers


def predict_user(user_data, pk):

    model_svm = joblib.load('content/models/model_svm.pkl')
    df = pd.DataFrame(user_data, columns=['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'Age', 'Sex'])

    prediction = model_svm.predict(df)[0]

    # Saving to DB
    save_user_prediction(prediction, pk)

    if prediction == 0:
        return "El usuario no parece tener rasgos de TEA."
    else:
        return "El usuario presenta rasgos característicos de TEA. Se sugiere realizar un análisis en profundidad."


def save_user_prediction(prediction, pk):
    user_profile = UserProfile.objects.get(user_id=pk)
    user_profile.tea = prediction
    user_profile.save(force_update=True)


def binarize_info(activity, info):
    if activity == 4:
        return False if info == 'A' or info == 'B' or info == 'C' else True
    else:
        return False if info == 'A' or info == 'B' else True


def binarize_answer(act):
    return act if act is None else act.answer


def update_model():
    print('Updating model...')
    patients = User.objects.filter(groups__name='Patients')
    new_data = []

    dataset_changed = False
    for p in patients:
        data = get_user_data(p.id)

        if data["TEA"] is not None and data["Guardado"] is False:
            dataset_changed = True
            print('There is new data. Adding to dataset...')

            ud = [
                0 if data["Actividad 1"] is False else 1,
                0 if data["Actividad 2"] is False else 1,
                0 if data["Actividad 3"] is False else 1,
                0 if data["Actividad 4"] is False else 1,
                0 if data["Actividad 5"] is False else 1,
                0 if data["Actividad 6"] is False else 1,
                0 if data["Información previa 1"] is False else 1,
                0 if data["Información previa 2"] is False else 1,
                0 if data["Información previa 3"] is False else 1,
                0 if data["Información previa 4"] is False else 1,
                data["Edad"],
                data["Género"],
                0 if data["TEA"] is False else 1
            ]

            new_data.append(ud)
            update_user_to_added(p.id)

    if dataset_changed:
        old_df = pd.read_csv('content/data/data.csv', index_col=[0])
        print(old_df.shape)
        new_df = pd.DataFrame(new_data,
                          columns=['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'Age', 'Sex', 'TEA'])

        result_df = pd.concat([old_df, new_df])
        print(result_df.shape)
        result_df.to_csv('content/data/data.csv')

        build_model()
    else:
        print('There is not new data to update.')


def update_user_to_added(pk):
    user_profile = UserProfile.objects.get(user_id=pk)
    user_profile.added_to_dataset = True
    user_profile.save(force_update=True)
