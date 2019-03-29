function Focus() {
    var tag=document.getElementById('i1');
    var val=tag.value;
    if(val=="请输入关键字"){
        tag.value='';
    }
}
function Blur() {
    var tag=document.getElementById('i1')
    var val=tag.value;
    if(val.length==0){
        tag.value="请输入关键字";
    }
}