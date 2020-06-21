function nao_animated_speech(speech, counter = 0) {

  let ui_text = "";
  let ajax_text = "";

  for (let i = 0; i < speech.length; i+=1) {
    ui_text += " " + speech[i].text;
    ajax_text += String.format(" ^start({0}) {1} ^wait({0})", speech[i].animation, speech[i].text)
  }

  $('#mytext').text(ui_text);

  $.ajax({
    url: '/nao_speech/',
    data: {
      'text': ajax_text,
      'speech_type': 'animated',
      'counter': counter,
    },
    dataType: 'json',
    success: function (data) {
      //alert("whatever")
    }
  });
}

function nao_action(action) {
  $.ajax({
    url: '/nao_action/',
    data: {
      'action': action,
    },
    dataType: 'json',
    success: function (data) {
      //alert("whatever")
    }
  });
}

if (!String.format) {
  String.format = function(format) {
    let args = Array.prototype.slice.call(arguments, 1);
    return format.replace(/{(\d+)}/g, function(match, number) {
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
        ;
    });
  };
}