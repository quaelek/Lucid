// static/js/animations.js
$(document).ready(function () {
    function showThinkingAnimation() {
      $(".thinking-animation").fadeIn(1000, function () {
        $(".thinking-animation").fadeOut(1000);
      });
    }
  
    function showEsotericLoader() {
      $(".esoteric-loader").fadeIn(1000);
    }
  
    function hideEsotericLoader() {
      $(".esoteric-loader").fadeOut(1000);
    }
  
    function slowWriteText(element, text, index) {
      if (index < text.length) {
        element.append(text[index++]);
        setTimeout(function () {
          slowWriteText(element, text, index);
        }, 35);
      }
    }
  
    $("form").on("submit", function (event) {
      event.preventDefault();
  
 
  
      showThinkingAnimation();
      showEsotericLoader();
  
      $.post("/interpret", {user_input: userInput}, function (data) {
        hideEsotericLoader();
        const assistantResponse = $(`<p><strong></strong> </p>`);
        $(".conversation").append(assistantResponse);
        slowWriteText(assistantResponse, data.content, 0);
        $("#user_input").val("");
      });
    });
  });
  
