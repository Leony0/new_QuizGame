//問題の送信ボタンを押したときに問題が登録される処理の実現
//今日は表示するところを実装する

console.log("JavaScriptが動作しています！");


const form = document.querySelector('form');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const question = document.querySelector('#question').value;

    const answer=[];
    let i=0;
    
    console.log(document.querySelector('#answer'+1).value);
    
    while(i<4){
        answer[i]=document.querySelector('#answer'+(i+1)).value;
        i++;
    }

    const correct = document.querySelector('#correct').value;

    window.alert("問題文："+question+"\n"+
        "回答："+answer[0]+","+answer[1]+","+answer[2]+","+answer[3]+"\n"+
        "正解："+correct
    );
    
});

