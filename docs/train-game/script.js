console.log("Matt script loaded");

const digitIndexs = [0, 1, 2, 3];
var prevContent = ['1','2','3','4']
var digitsValid = [true,true,true,true]

// hide solution iframe at first
window.addEventListener("load",function(){
   var el = document.getElementById("result_frame");
   if (! el.src){
      el.style.display = "none";
   }
   el.addEventListener("load",function(){
      console.log("iframe loaded");
      el.style.display = "inline";
   });
});

window.addEventListener("load",function(){
   console.log("Triggering main matt script");
   digitIndexs.forEach(function(digitIndex) {
       console.log("Attaching event watch for digit " + digitIndex);
       var el = document.getElementById('digit-' + digitIndex);
       el.onkeydown = function(e){preType(e,digitIndex,el)};
       el.onkeyup = function(e){typed(e,digitIndex,el)};
       el.addEventListener("focus",function(){selectText(el)});
   });
   var targetEl = document.getElementById('target')
   targetEl.onkeyup = function(){
      var buttonEl = document.getElementById('submit');
      if (targetEl.value.length == 0){
         targetEl.classList.add('invalid');
      }else{
         targetEl.classList.remove('invalid');
      }
      if(inputsValid()){
         buttonEl.classList.remove('button-disable');
      }else{
         buttonEl.classList.add('button-disable');
      }
   };
   console.log("Finished setting up digit watchers");
},false);

function selectText(el){
   el.selectionStart = 0;
   el.selectionEnd = el.value.length;
}

function preType(event,digitIndex,digitEl){
   prevContent[digitIndex] = digitEl.value;
   if ((event.code.toLowerCase().startsWith("digit")) || (event.code.toLowerCase().startsWith("key"))){
      digitEl.value = "";
   }
}

function typed(event,digitIndex,digitEl){
   console.log("Typed " + event.code + " for digit " + digitIndex);
   console.log("Digit " + digitIndex + " has contents " + digitEl.value + " with length "+ digitEl.value.length);


   if((digitEl.value[0] < '0') || ('9' < digitEl.value[0])){
      console.log("Number in text field");
      digitEl.value = prevContent[digitIndex];
      selectText(digitEl);
   }

   // just in case
   if (digitEl.value.length > 1){
      digitEl.value = digitEl.value[0];
   }


   if (digitEl.value.length == 0){
      digitEl.classList.add("invalid");
      digitsValid[digitIndex] = false;
      console.log("Disabling button");
      document.getElementById("button").classList.add('button-disable');
      selectText(digitEl);
   }else{
      console.log("Text length is now 1 = " + digitEl.value.length);
      digitEl.classList.remove("invalid");
      digitsValid[digitIndex] = true;
      if (inputsValid()){
         console.log("Enabling button");
         document.getElementById('button').classList.remove('button-disable');
      }
      if ((digitIndex < 3) && (event.code.toLowerCase().startsWith("digit"))){
         var nextEl = document.getElementById('digit-' + (digitIndex+1));
         nextEl.focus();
         selectText(nextEl);
      }
   }

}

function inputsValid(){
   var valid = true;
   digitIndexs.forEach(function(digitIndex) {
      valid &= digitsValid[digitIndex];
   });
   valid &= (document.getElementById('target').value.length > 0);
   return(valid);
}
