---
layout: post
title: Video Script UI 💡
description: Interactive UI for Generating Scripts
type: post
comments: false
permalink: Generator
categories: [Final Project]
---


<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Video Script Generator</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
  <style>
    html, body {
    margin: 0;
    padding: 60px 20px;
    font-family: 'Inter', sans-serif;
    color: white;
    background: #0e0e0e;
    overflow-x: hidden;
    min-height: 100vh;
    position: relative;
    box-sizing: border-box;
    }

    canvas#background {
      position: fixed;
      top: 0;
      left: 0;
      z-index: -10;
      width: 100%;
      height: 100%;
    }

    h1 {
      font-size: 2.8rem;
      font-weight: 600;
      margin-bottom: 20px;
      text-align: center;
      color: #ffffff;
      animation: fadeIn 1.2s ease;
    }

    .glass-card {
      background: rgba(255, 255, 255, 0.06);
      backdrop-filter: blur(15px);
      border-radius: 20px;
      padding: 40px 30px;
      width: 90%;
      max-width: 480px;
      box-shadow: 0 8px 40px rgba(0, 0, 0, 0.3);
      text-align: center;
      animation: fadeIn 1.5s ease;
    }

    input {
      width: 100%;
      padding: 14px;
      margin-top: 15px;
      font-size: 1rem;
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.2);
      background-color: rgba(255, 255, 255, 0.05);
      color: white;
      outline: none;
      transition: 0.3s ease;
    }

    input::placeholder {
      color: #ccc;
    }

    input:focus {
      border-color: #00ffe7;
      background-color: rgba(255, 255, 255, 0.08);
    }

    .submit-btn {
      margin-top: 20px;
      width: 100%;
      padding: 14px;
      font-size: 1rem;
      font-weight: bold;
      border: none;
      border-radius: 10px;
      background: linear-gradient(135deg, #00ffe7, #00d4ff);
      color: black;
      cursor: pointer;
      transition: transform 0.2s ease;
    }

    .submit-btn:hover {
      transform: scale(1.03);
    }

    .card-result {
      margin-top: 30px;
      padding: 25px;
      border-radius: 15px;
      background: rgba(255, 255, 255, 0.07);
      backdrop-filter: blur(10px);
      color: white;
      text-align: left;
      animation: fadeIn 1s ease;
      width: 90%;
      max-width: 600px;
    }

    .card-result a {
      text-decoration: none;
      color: #00ffe7;
      font-weight: bold;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @media screen and (max-width: 600px) {
      h1 { font-size: 2rem; }
      .glass-card { padding: 25px 20px; }
    }

    .main-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 1000px;
    margin: 0 auto;
    }

    .loader {
    border: 4px solid rgba(255, 255, 255, 0.1);
    border-top: 4px solid #00ffe7;
    border-radius: 50%;
    width: 26px;
    height: 26px;
    animation: spin 1s linear infinite;
    display: inline-block;
    vertical-align: middle;
    margin-left: 10px;
    }

    @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
    }


  </style>
</head>
<body>

<canvas id="background"></canvas>

<div class="main-content">
  <h1>🎬 Video Script Generator</h1>
  <div class="glass-card">
    <input type="text" id="keywordInput" placeholder="Enter a potential video topic" />
    <button class="submit-btn" id="generateBtn" onclick="submitKeyword()">Generate</button>
    </div>
  <div class="card-result" id="trendingSection">
  <h2>🔥 Trending Today</h2>
  <ul id="trendingList"></ul>
    </div>
  <div id="scriptsContainer"></div>
</div>


<script>
  const sheetURL = "https://opensheet.vercel.app/15jwGTstUvwavtcD44ZNMk6RDOs2y7zcn3hHFvvw691M/Sheet1";
  const webhookURL = "https://hook.us2.make.com/nqoi4abb8zblgrchy7y9vosnqhrs1pes";

  function clean(str) {
    return str?.toLowerCase().replace(/^['"`“”‘’]+|['"`“”‘’]+$/g, '').replace(/\s+/g, ' ').replace(/[\u200B-\u200D\uFEFF]/g, '').trim();
  }

  async function submitKeyword() {
        const inputEl = document.getElementById("keywordInput");
        const btnEl = document.getElementById("generateBtn");
        const keyword = clean(inputEl.value);
        const container = document.getElementById("scriptsContainer");

        if (!keyword) return alert("Please enter a keyword.");

        // Show loading state
        btnEl.disabled = true;
        btnEl.innerHTML = `Generating <span class="loader"></span>`;

        // Send to webhook
        await fetch(webhookURL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ keyword })
        });

        // Estimate new row number
        let estimatedRow = "a new row";
        try {
            const res = await fetch(sheetURL);
            const data = await res.json();
            estimatedRow = `Row ${data.length + 1}`;
        } catch (err) {
            console.warn("Unable to fetch sheet data.");
        }

        // Show result
        container.innerHTML = `
            <div class="card-result">
            <h2>✅ Request Sent</h2>
            <p>Your script is being generated.</p>
            <p><strong>Check:</strong> ${estimatedRow}</p>
            <a href="https://docs.google.com/spreadsheets/d/15jwGTstUvwavtcD44ZNMk6RDOs2y7zcn3hHFvvw691M/edit#gid=0" target="_blank">📄 View Script on Google Sheets</a>
            </div>
        `;

        // Optional: Reset button after 2s
        setTimeout(() => {
            btnEl.disabled = false;
            btnEl.innerHTML = "Generate";
            inputEl.value = "";
        }, 2000);
    }

</script>

<!-- 🎇 Fullscreen Animated Particles Background -->
<script>
  const canvas = document.getElementById("background");
  const ctx = canvas.getContext("2d");
  let width = canvas.width = window.innerWidth;
  let height = canvas.height = window.innerHeight;

  window.addEventListener("resize", () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    initParticles();
  });

  let particles = [];
  const colors = ['#00ffe7', '#00d4ff', '#a5f3fc', '#67e8f9'];

  function initParticles() {
    particles = [];
    for (let i = 0; i < 100; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 2 + 1,
        dx: (Math.random() - 0.5) * 0.7,
        dy: (Math.random() - 0.5) * 0.7,
        color: colors[Math.floor(Math.random() * colors.length)]
      });
    }
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);
    particles.forEach(p => {
      p.x += p.dx;
      p.y += p.dy;

      if (p.x < 0 || p.x > width) p.dx *= -1;
      if (p.y < 0 || p.y > height) p.dy *= -1;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.fill();
    });

    requestAnimationFrame(animate);
  }

  initParticles();
  animate();
</script>

<script>
  const trendsWebhook = "https://hook.us2.make.com/nfg5v5s414bmvb08oxxlbyeb2acc8byc";

  async function loadTrendingVideos() {
    const list = document.getElementById("trendingList");
    list.innerHTML = "<li>Loading trends...</li>";

    try {
      const res = await fetch(trendsWebhook);
      const text = await res.text();

      // Fix invalid JSON manually
      let trends = [];

      // Try to extract all valid object blocks from the malformed JSON
      const regex = /{[^{}]*"text"[^{}]*"diggCount"[^{}]*"webVideoUrl"[^{}]*}/g;
      const matches = text.match(regex);

      if (matches) {
        trends = matches.map(str => {
          try {
            return JSON.parse(
              str
                .replace(/([{,])\s*([a-zA-Z0-9_]+)\s*:/g, '$1"$2":') // quote keys
                .replace(/:\s*'([^']+)'/g, ': "$1"') // single quotes to double
                .replace(/:\s*“([^”]+)”/g, ': "$1"') // fancy quotes
                .replace(/:\s*”([^“]+)“/g, ': "$1"') // reverse fancy quotes
            );
          } catch (e) {
            return null;
          }
        }).filter(Boolean);
      }

      if (trends.length === 0) {
        list.innerHTML = "<li>No trends available right now.</li>";
        return;
      }

      list.innerHTML = trends.slice(0, 5).map(t => `
        <li>
          <a href="${t.webVideoUrl}" target="_blank">
            🎥 ${t.text}<br>❤️ ${t.diggCount?.toLocaleString?.() || 0}
          </a>
        </li>
      `).join("");

    } catch (err) {
      list.innerHTML = "<li>Unable to load trends.</li>";
      console.error("Trend load error:", err);
    }
  }

  loadTrendingVideos();
</script>



</body>
</html>
