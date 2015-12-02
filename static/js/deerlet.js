
//$(".editormd-markdown-textarea").autoSave(function() {
//    //var time = new Date().getTime();
//    //$("#msg").text("Draft Autosaved " + time);
//    console.log('doubi');
//}, 500);


function saveToFile() {
    var resume = $('.editormd-markdown-textarea')[0].value;
    $.ajax({
        url: "/save",
        type: 'PUT',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(resume, null, '\t'),
        success: function (res) {
            if (res.code == 1) {
                console.log('')
            } else {
                alert('管理密码错误');
                location.reload();
            }
        }
    })
}

//var autosaveOn = false;
//
//function myAutosavedTextbox_onTextChanged()
//{
//    if (!autosaveOn)
//    {
//        autosaveOn = true;
//
//        $('textarea').eq(0).everyTime("300000", function(){
//             $.ajax({
//                 type: "POST",
//                 url: "/save",
//                 data: JSON.stringify("id=1", null, '\t'),
//                 success: function(msg) {
//                     $('#autosavenotify').text(msg);
//                 }
//             });
//        }); //closing tag
//    }
//}

function validate_read_pass() {
    var readPassword = $("input[name='read_password']")[0].value;
    $.ajax({
        url: "/validate",
        type: 'POST',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(readPassword, null, '\t'),
        success: function (res) {
            if (res.code == 1) {
                location.reload();
            } else {
                alert('阅读密码错误');
            }
        }
    })
}


function validate_admin_pass() {
    var adminPassword = $("input[name='admin_password']")[0].value;
    $.ajax({
        url: "/validate_admin",
        type: 'POST',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(adminPassword, null, '\t'),
        success: function (res) {
            if (res.code == 1) {
                location.reload();
            } else {
                alert('管理密码错误');
            }
        }
    })
}

