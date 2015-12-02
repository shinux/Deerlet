
function saveToFile() {
    var resume = $('.editormd-markdown-textarea').val();
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

//setInterval("saveToFile()", 6000);


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

