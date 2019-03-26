alert("文件外部")
function fun() {
    var tag = document.getElementById("i1");
     // 获取内容
    var content = tag.innerText;
    var f = content.charAt(0);
    var l = content.substring(1,content.length);
    var new_content = l+f;
    tag.innerText = new_content;
}
setInterval("fun()",500);