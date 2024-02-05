---
layout: base
title: "Quizzes"
summary: "ESB Quizzes"
toplevel: Resources
# toplevellink: /resources
---

   
<h5>Available Now</h5>
  <ul style="text-align: left;">
<li><a href="https://docs.google.com/forms/d/e/1FAIpQLSfhy0FaXG4jYarmYzp4Kz3ImbUg8QBC6fOy-G-9Trx6lcdIZQ/viewform">Inputs, Outputs, Outcomes Quiz</a>&nbsp;</li>
  </ul><br/> 
  
  
<h5>Coming Soon</h5>
<ul style="text-align: left;">
  <li>Time Use Evaluation Quiz (coming June 2024)</li>
  <li>Effective Goals Quiz (coming June 2024)</li>
</ul>





<div id="subscription"> <!--if the home page is requested, a subscription form is populated here from javascript below (though you won't literally see the code here since it runs after page load--></div>


<!--HTML for Quiz-->
<!--<div id="quiz">
  <h1>Quiz</h1>
  <form id="quiz-form">
<div id="question1">
  <p>What is the capital of France?</p>
  <input id="q1a" name="q1" type="radio" value="a" />
  <label>Paris</label><br />
  <input id="q1b" name="q1" type="radio" value="b" />
  <label>London</label><br />
  <input id="q1c" name="q1" type="radio" value="c" />
  <label>Rome</label><br />
  <input id="q1d" name="q1" type="radio" value="d" />
  <label>Madrid</label><br />
</div>
<br />
<div id="question2">
  <p>What is the capital of Japan?</p>
  <input id="q2a" name="q2" type="radio" value="a" />
  <label>Tokyo</label><br />
  <input id="q2b" name="q2" type="radio" value="b" />
  <label>Beijing</label><br />
  <input id="q2c" name="q2" type="radio" value="c" />
  <label>Seoul</label><br />
  <input id="q2d" name="q2" type="radio" value="d" />
  <label>Bangkok</label><br />
</div>
<br />
<div id="question3">
  <p>What is the capital of Australia?</p>
  <input id="q3a" name="q3" type="radio" value="a" />
  <label>Sydney</label><br />
  <input id="q3b" name="q3" type="radio" value="b" />
  <label>Melbourne</label><br />
  <input id="q3c" name="q3" type="radio" value="c" />
  <label>Brisbane</label><br />
  <input id="q3d" name="q3" type="radio" value="d" />
  <label>Canberra</label><br />
</div>
<br />
<input type="submit" value="Submit" />
<input type="reset" value="Reset" />
  </form>
  <div id="results"></div>
</div>-->
<!--JavaScript for Quiz-->
<script>
<!--
  // Store correct answers in an array
  var answers = ["a", "a", "d"];

  // Add event listener to quiz form
  var quizForm = document.getElementById("quiz-form");
  quizForm.addEventListener("submit", function(event)
  event.preventDefault(); // Prevent form from being submitted

// Check answers
var correct = 0;
var incorrect = 0;
for (var i = 0; i < answers.length; i++) {
  var radioName = "q" + (i + 1);
  var radios = document.getElementsByName(radioName);
  for (var j = 0; j < radios.length; j++) {
if (radios[j].checked && radios[j].value === answers[i]) {
  correct++;
} else if (radios[j].checked) {
  incorrect++;
}
  }
}

// Display results
var resultsDiv = document.getElementById("results");
resultsDiv.innerHTML = "Correct: " + correct + "<br>Incorrect: " + incorrect;
  });
-->
</script>




