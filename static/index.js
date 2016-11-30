$(document).ready(function(){
    var clipboard = new Clipboard('.btn-copy');
    clipboard.on('success', function(e) {
        console.log(e);
    });
    clipboard.on('error', function(e) {
        console.log(e);
    });

    $(".btn-copy").click(function(e){
        e.preventDefault();
        var btnHref = $(this).attr('href')
        var item = $(this)
        item.text("已复制")
        item.removeClass('btn-primary')
        item.addClass('btn-success')

        setTimeout(function(){
            item.text("Copy")
            item.removeClass('btn-success')
            item.addClass('btn-primary')
        }, 5000)
    })
})


function check(form) {
    if(form.longurl.value=='') {
        alert("请输入URL");
        return false;
        }
    var str=form.longurl.value;
    var Expression=/http(s)?:\/\/([\w-]+\.)+[\w-]+(\/[\w- .\/?%&=]*)?/;
    var objExp=new RegExp(Expression);
    if(objExp.test(str)!=true){
        alert('请输入合法的url如 http://xxx.xxx');
        return false;
        }
    document.myform.submit();
    }
