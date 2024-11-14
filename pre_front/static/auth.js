document.getElementById("touroku").onclick = function(event) {
    const name = document.getElementById("name").value;
    const pass = document.getElementById("pass").value;
    const repass = document.getElementById("repass").value;
    let flag = 0;

    if (name.length === 0) { flag = 1; }
    if (pass.length === 0) { flag = 1; }
    if (repass.length === 0) { flag = 1; }

    if (flag === 1) {
        alert('必須項目が未記入の箇所があります');
        event.preventDefault();
    } else {
        var regexp = /^([a-zA-Z0-9]{8,})$/;
        if (!regexp.test(pass)) {
            alert('パスワードが半角英数8文字以上になっていません');
            event.preventDefault();
        } else if (pass !== repass) {
            alert('パスワードが再入力時と違っています');
            event.preventDefault();
        }
    }
};
