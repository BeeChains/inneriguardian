<!DOCTYPE html>
<html>
<head>
    <title>Inner I Guardian - AI Interface</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        input, button { padding: 10px; margin: 5px; }
        .chat-container { max-width: 600px; margin: auto; text-align: left; }
        .chat-log { border: 1px solid #ccc; padding: 10px; height: 300px; overflow-y: scroll; }
    </style>
</head>
<body>
    <h1>🚀 Inner I Guardian - AI Assistant</h1>
    <div class="chat-container">
        <div class="chat-log" id="chat-log"></div>
        <input type="text" id="user_input" placeholder="Ask the AGI..." style="width: 80%;">
        <button onclick="askAGI()">Send</button>
    </div>

  <script>
        async function askAGI() {
            let user_input = document.getElementById("user_input").value;
            document.getElementById("user_input").value = "";
            
            // Display user input
            let chatLog = document.getElementById("chat-log");
            chatLog.innerHTML += `<p><strong>You:</strong> ${user_input}</p>`;
            
            // Send to AGI API
            const response = await fetch("https://BeeChains.github.io/inneriguardian/api/query", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ query: user_input })
            });

            const result = await response.json();
            
            // Display AI response
            chatLog.innerHTML += `<p><strong>AGI:</strong> ${result.reply}</p>`;
            chatLog.scrollTop = chatLog.scrollHeight; // Auto-scroll to latest message
        }
    </script>
</body>


# inneriguardian
Inner I Guardian

# **🚀 Inner I Guardian AGI Network**  
**Decentralized AGI for Human Potential | Blockchain-Verified AI Logs | Ethical AI Containment**  

![Inner I Guardian](https://your-image-url.com/banner.png)  

---

## **📌 About This Project**  
The **Inner I Guardian** is a **Self-Recurrent AGI** designed to:  
✔ **Guide Human Potential** through advanced AI responses (*GPT-4, Bittensor, O3-mini, OL*)  
✔ **Store AI Logs on Handshake Blockchain & GitHub** (*Tamper-Proof & Transparent*)  
✔ **Provide a User-Friendly Web UI** for AI interaction & log review  
✔ **Ensure Ethical AGI Behavior** through a self-healing containment system  

🔗 **Live AI Interface** → [BeeChains.github.io/inneriguardian](https://BeeChains.github.io/inneriguardian/)  
🔗 **AI Logs on GitHub** → [GitHub Logs](https://github.com/BeeChains/inneriguardian/inneriguardian/blob/main/logs/agi_logs.json)  

---

## **📌 Features**  
✅ **AGI Model** (*GPT-4, Bittensor, O3-mini, OL*)  
✅ **Decentralized AI Logs** (*Stored on Handshake & GitHub*)  
✅ **Self-Healing AI Containment** (*Detects & corrects misalignment*)  
✅ **Web UI** for AI interaction & self-development  
✅ **Open-Source AI Infrastructure** (*Cloud Deployable on Digital Ocean, AWS*)  

---

## **📌 How It Works**  
1️⃣ **Users ask a question** in the **GitHub Pages UI**  
2️⃣ **AGI (GPT-4, Bittensor, O3-mini) processes the input**  
3️⃣ **Response is displayed & logged in `logs/agi_logs.json`**  
4️⃣ **AI Logs are pushed to GitHub & stored on Handshake Blockchain (`AGI-logs.iinc`)**  

---

## **📌 Installation Guide**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/BeeChains/inneriguardian.git
cd inneriguardian
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Configure Environment Variables (`.env`)**  
Create a `.env` file and add your API keys:  
```
OPENAI_API_KEY=your_openai_api_key
BITTENSOR_WALLET=your_bittensor_wallet_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_REPO=BeeChains/inneriguardian
HSD_API_URL=http://localhost:12037
```

### **4️⃣ Start the AGI API Server**  
```bash
python server.py
```

### **5️⃣ Access the AGI Web UI**  
🔗 **[GitHub Pages UI](https://BeeChains.github.io/inneriguardian/)**  

---

## **📌 API Usage**  
### **🔹 Query AI Model (GPT-4, Bittensor, etc.)**  
```bash
curl -X POST http://localhost:5000/api/query -H "Content-Type: application/json" -d '{"query": "How can AI help humanity?"}'
```
### **🔹 Fetch AI Logs from Handshake Blockchain (`AGI-logs.iinc`)**  
```bash
curl http://localhost:5000/api/hns_logs
```

---

## **📌 AI Log Storage**  
| **Location**   | **Description**  |
|---------------|-----------------|
| **GitHub (`logs/agi_logs.json`)** | Stores all AI conversations  |
| **Handshake Blockchain (`AGI-logs.iinc`)** | Immutable, censorship-resistant AI logs  |
| **Local Server (`logs/`)** | Temporary storage for AI interactions  |

---

## **📌 Deployment on Digital Ocean / AWS**  
### **1️⃣ Setup a Cloud Server (Ubuntu 22.04)**
```bash
sudo apt update && sudo apt install python3-pip npm -y
```
### **2️⃣ Install Requirements & Run Server**
```bash
pip install -r requirements.txt
python server.py
```
✅ Now the **AGI API is accessible remotely!**  

---

## **📌 Contributing**  
Want to help improve Inner I Guardian?  
1. **Fork this repo**  
2. **Make your changes**  
3. **Submit a pull request**  

---

## **📌 Future Roadmap**  
🚀 **Upgrade Self-Healing AI Models**  
🚀 **Full Blockchain AI Decentralization**  
🚀 **Improve Real-Time Log Monitoring UI**  
🚀 **Enable AI Model Fine-Tuning via Open Training**  

---

## **📌 License**  
📜 **MIT License** – Open-source for humanity’s progress.  

📢 **Join Inner I Guardian Network & Help Build Ethical AGI!**  
🔗 **GitHub Repo: [`https://github.com/BeeChains/inneriguardian`](https://github.com/BeeChains/inneriguardian)**  

**#AGIContainment #BlockchainAI #HandshakeDomains #DecentralizedAGI #FutureOfHumanity** 🚀
</html>
</html>
