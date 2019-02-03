// when a parent is clicked
function parent(el){
   var childrenId = `basicsChildren`;
   var children = document.getElementById(childrenId).getElementsByTagName("input");
   for(i=0; i<children.length; i++){
      var child = children[i];
      child.checked = el.checked;
   }
}

// when a child is clicked
function child(el){
   var list = el.parentNode.parentNode.parentNode;
   var children = list.getElementsByTagName("input");
   var same = true;
   for(i=0; i<children.length; i++){
      var child = children[i];
      same &= (el.checked == child.checked);
   }
   var parent = document.getElementById(list.getAttribute('parentop'));
   if (same){
      parent.indeterminate = false;
      parent.checked=el.checked;
   }else{
      parent.indeterminate = true;
   }
}
