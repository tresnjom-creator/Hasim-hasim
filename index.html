<!DOCTYPE html>
<html lang="bs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hashim</title>
    <style>
        body {
            background-color: #131314;
            color: #e3e3e3;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 16px;
            display: flex;
            flex-direction: column;
            height: 100vh;
            box-sizing: border-box;
        }
        .header {
            border-bottom: 1px solid #333538;
            padding-bottom: 12px;
            margin-bottom: 15px;
        }
        h2 { margin: 0; color: #ffffff; font-size: 22px; }
        p { color: #8e918f; font-size: 13px; margin: 5px 0 0 0; }
        
        .chat-container {
            flex: 1;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 12px;
            padding-bottom: 20px;
        }
        .message {
            background-color: #1e1f20;
            border: 1px solid #333538;
            border-radius: 16px;
            padding: 14px;
            max-width: 90%;
            line-height: 1.5;
            font-size: 14px;
        }
        .user-message {
            background-color: #004a77;
            align-self: flex-end;
            border: none;
        }
        .input-area {
            border-top: 1px solid #333538;
            padding-top: 12px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        textarea {
            width: 100%;
            height: 70px;
            background-color: #1e1f20;
            color: #e3e3e3;
            border: 1px solid #333538;
            border-radius: 12px;
            padding: 12px;
            box-sizing: border-box;
            font-size: 14px;
            resize: none;
        }
        .controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .sports {
            display: flex;
            gap: 15px;
            font-size: 13px;
            color: #c4c7c5;
        }
        button {
            background-color: #a8c7fa;
            color: #001d35;
            border: none;
            padding: 10px 22px;
            font-size: 14px;
            font-weight: bold;
            border-radius: 20px;
            cursor: pointer;
        }
        button:hover { background-color: #d3e3fd; }
    </style>
</head>
<body>

<div class="header">
    <h2>🧠 Hashim</h2>
    <p>Tvoj lični AI sportski analitičar.</p>
</div>

<div class="chat-container" id="chatContainer">
    <div class="message">
        Zdravo Merzuhe! Ja sam Hashim. Ubaci parove koje želiš da analiziramo (možeš i 10 parova odjednom, svaki u novi red), izaberi sport i posalji mi poruku!
    </div>
</div>

<div class="input-area">
    <div class="sports">
        <label><input type="radio" name="sport" value="fudbal" checked> Fudbal ⚽</label>
        <label><input type="radio" name="sport" value="kosarka"> Košarka 🏀</label>
    </div>
    <textarea id="userInput" placeholder="Unesi parove (svaki u novi red)..."></textarea>
    <div class="controls">
        <span></span>
        <button onclick="posaljiPoruku()">Pošalji</button>
    </div>
</div>

<script>
function posaljiPoruku() {
    const input = document.getElementById('userInput');
    const text = input.value.trim();
    if (!text) return;
    
    const chat = document.getElementById('chatContainer');
    
    // Korisnikova poruka
    const userMsg = document.createElement('div');
    userMsg.className = 'message user-message';
    userMsg.innerText = text;
    chat.appendChild(userMsg);
    
    input.value = '';
    chat.scrollTop = chat.scrollHeight;
    
    // Hashimov odgovor
    setTimeout(() => {
        const sport = document.querySelector('input[name="sport"]:checked').value;
        const parovi = text.split('\n').filter(p => p.trim() !== '');
        
        let odgovor = "Evo rezultata simulacije za tvoj tiket:<br><br>";
        parovi.forEach((par, index) => {
            const pDom = Math.floor(Math.random() * 18) + 42;
            const pGost = Math.floor(Math.random() * 18) + 20;
            const pNer = 100 - (pDom - pGost);
            
            if (sport === 'fudbal') {
                const golovi = Math.floor(Math.random() * 25) + 62;
                odgovor += `<b>${index + 1}. ${par}</b><br>• 1: ${pDom}% | X: ${pNer}% | 2: ${pGost}%<br>• 🔥 Over 2.5: <b>${golovi}%</b><br><br>`;
            } else {
                const adjDom = (pDom + pNer / 2).toFixed(1);
                const adjGost = (pGost + pNer / 2).toFixed(1);
                const margina = Math.floor(Math.random() * 68) + 154;
                odgovor += `<b>${index + 1}. ${par}</b><br>• Pobjeda domaćina: ${adjDom}%<br>• Pobjeda gosta: ${adjGost}%<br>• 🔥 Margina koševa: <b>~${margina}</b><br><br>`;
            }
        });
        
        const botMsg = document.createElement('div');
        botMsg.className = 'message';
        botMsg.innerHTML = odgovor;
        chat.appendChild(botMsg);
        chat.scrollTop = chat.scrollHeight;
    }, 800);
}
</script>

</body>
</html>

