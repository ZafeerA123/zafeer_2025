---
layout: base
title: Student Home 
description: Home Page
hide: true
image: /images/mario_animation.png
comments: true
---

<table cellpadding="10">
    <tr>
        <td><a href="{{site.baseurl}}/HWtable"><strong>Homework Table</strong></a></td>
        <td><a href="{{site.baseurl}}/ToolsJourney">Tools Journey</a></td>
        <td><a href="{{site.baseurl}}/Sprint1TSDP">Partner Check</a></td>
        <td><a href="{{site.baseurl}}/final">Final Review (tri 2) Table</a></td>
        <td><a href="{{site.baseurl}}/Blog_5">Sprint 5 Dynamic Checkpoint Blog</a></td>
    </tr>
</table>


<div style="align-items: center; display: flex; flex-direction: column;">
    <a href="{{site.baseurl}}/">
        <img src="{{site.baseurl}}/images/globe.gif" height="60" title="Globe [:" alt="" style="margin-top: -140px; margin-left: 880px;">
    </a>
</div>

<!-- 3-Box Socials Section -->
<div class="socials-section d-flex justify-content-between flex-wrap" style="gap: 40px;">

    <!-- Box 1: Email + GitHub Frontend + Backend -->
  <div class="socials-box" style="flex: 1; min-width: 240px;">
    <h2>Get in Touch</h2>
    <div class="d-flex flex-column align-items-center gap-3 mt-4">
      <a href="mailto:optivize47@gmail.com" class="btn btn-social-blue" target="_blank">📧 Email</a>
      <a href="https://github.com/ZafeerA123" class="btn btn-social-blue" target="_blank">GitHub Profile</a>
      <a href="https://www.canva.com/design/DAGqEWK7Il8/Z_WJz8o5X49zJNm5sdKb3Q/edit?utm_content=DAGqEWK7Il8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton" class="btn btn-social-blue" target="_blank">Resume</a>
    </div>
  </div>


  <!-- Box 2: LinkedIn Logo -->
  <div class="socials-box" style="flex: 1; min-width: 240px;">
    <h2>LinkedIn</h2>
    <a href="https://www.linkedin.com/in/zafeer-ahmed-ocs/" target="_blank">
      <img src="{{ site.baseurl }}/images/linkedin.png" alt="LinkedIn Logo" class="linkedin-logo mt-3">
    </a>
  </div>

  <!-- Box 3: QR Code -->
  <div class="socials-box text-center" style="flex: 1; min-width: 240px;">
    <h2>Scan My QR</h2>
    <p style="color: #fff;"></p>
    <img src="{{ site.baseurl }}/images/qr.jpg" alt="Optivize QR Code" class="qr-code mt-3">
  </div>

</div>


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Home!</title>
    <style>
      .fade-in {
        opacity: 0;
        animation: fadeIn 2s forwards;
      }
      @keyframes fadeIn {
        to {
          opacity: 1;
        }
      }
      .reveal-later {
        opacity: 0;
        transition: opacity 1s;
        animation-delay: 2s;
        animation-fill-mode: forwards;
      }
      /* Button styling */
      .cool-button {
        background: linear-gradient(to right, #ff7e5f, #feb47b); /* Same gradient as other button */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px; /* Rounded edges */
      }
      .cool-button:hover {
        background-color: #45a049; /* Darker green on hover */
      }
      /* Gradient button styling */
      .gradient-button {
        background: linear-gradient(to right, #ff7e5f, #feb47b); /* Gradient colors */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px; /* Rounded edges */
      }
      /* Transparent div box with orange border */
      .transparent-box {
        background-color: transparent;
        border: 2px solid orange;
        padding: 20px;
        margin-top: 10px;
      }
      @keyframes slideIn {
        from {
          transform: translateX(100%); /* Start off-screen to the right */
          opacity: 0;
        }
        to {
          transform: translateX(0); /* End in its normal position */
          opacity: 1;
        }
      }
      /* Apply sliding animation to the div boxes */
      .transparent-box {
        background-color: transparent;
        border: 2px solid orange;
        padding: 20px;
        margin-top: 10px;
        opacity: 0;
        animation: slideIn 2s forwards; /* Slide in animation */
      }
      /* You can also define different animation delays if you want the boxes to slide in sequentially */
      .transparent-box:nth-child(1) {
        animation-delay: 0.5s;
      }
      .transparent-box:nth-child(2) {
        animation-delay: 2s;
      }
      /* Styles for the arrow and text */
      .arrow-text-container {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -150%); /* Adjust positioning */
        text-align: center;
      }
      .arrow {
        width: 0;
        height: 0;
        border-left: 10px solid transparent;
        border-right: 10px solid transparent;
        border-bottom: 20px solid black; /* Arrow color */
        margin: 0 auto;
      }
      .arrow-text {
        font-size: 20px;
        color: black; /* Text color */
        margin-top: 5px;
      }
      .socials-section {
        background: rgba(255, 221, 0, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 50px auto;
        max-width: 1000px;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        gap: 40px;
      }
      .socials-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        text-align: center;
        flex: 1;
        min-width: 240px;
      }
      .socials-box h2 {
        background: linear-gradient(135deg, #ffdd00, #fbb034);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        margin-bottom: 20px;
      }
      .btn-social-blue {
        background-color: #3498db;
        color: #fff;
        font-weight: bold;
        border: none;
        padding: 12px 20px;
        border-radius: 8px;
        text-decoration: none;
        width: 200px;
        text-align: center;
        transition: all 0.3s ease;
      }
      .btn-social-blue:hover {
        background-color: #5dade2;
        transform: translateY(-3px) scale(1.05);
      }
      .qr-code {
        width: 180px;
        height: 180px;
        border-radius: 12px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 2px solid #fbb034;
      }
      .qr-code:hover {
        transform: scale(1.2);
        box-shadow: 0 0 20px #fbb034;
      }
      /* LinkedIn Logo */
      .linkedin-logo {
        width: 100px;
        height: 100px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-radius: 12px;
        border: 2px solid #0077b5;
      }
      .linkedin-logo:hover {
        transform: scale(1.15);
        box-shadow: 0 0 15px #0077b5;
      }
    </style>
</head>
<body>
    <!-- First div with the gradient button -->
      <div class="socials-section d-flex flex-column align-items-center text-center" style="margin-top: 40px;">
    <h2>Final Blogs for OCS - Tri 3</h2>
    <p style="color: #fff;">Explore my reflections, checkpoints, and project summaries from the last trimester of Optivize development.</p>
    <div class="d-flex flex-column align-items-center gap-3 mt-3">
      <button class="gradient-button" onclick="window.location.href='{{site.baseurl}}/Blog_Optivize'">Final Blog</button>
      <button class="gradient-button" onclick="window.location.href='{{site.baseurl}}/StudyBlog'">Homework Certificates</button>
    </div>
  </div>
    <!-- Second div with the "Past Projects" button and video -->
    <div class="transparent-box" style="display: flex; align-items: center; justify-content: flex-start;">
        <!-- Embedded video with custom thumbnail -->
        <video width="320" height="240" controls poster="{{site.baseurl}}/images/gif1.gif" style="margin-right: 10px;">
            <source src="{{site.baseurl}}/images/Video1.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <p>Watch this video to see my past projects!</p>
        <!-- Button for past projects -->
        <button class="cool-button" onclick="window.open('https://zafeera123.github.io/Personal2/', '_blank')">Past Projects</button>
    </div>

</body>
</html>

<br>

Go to My About Page 
<!-- Button element -->
<button class="cool-button" onclick="window.open('https://zafeera123.github.io/zafeer_2025/about/', '_blank')">About Me</button>



{% assign sprite_file = site.baseurl | append: page.image %}  <!--- Liquid concatentation --->  
{% assign hash = site.data.mario_metadata %}  <!--- Liquid list variable created from file containing mario metatdata for sprite --->  
{% assign pixels = 256 %} <!--- Liquid integer assignment --->

<!--- HTML for page contains <p> tag named "mario" and class properties for a "sprite"  -->
<p id="mario" class="sprite"></p>

<!--- Embedded Cascading Style Sheet (CSS) rules, defines how HTML elements look --->  
<style>  
  /*CSS style rules for the elements id and class above...*/  
  .sprite {  
    height: {{pixels}}px;  
    width: {{pixels}}px;  
    background-image: url('{{sprite_file}}');  
    background-repeat: no-repeat;  
  }  
  
  /*background position of sprite element*/  
  #mario {  
    background-position: calc({{animations[0].col}} * {{pixels}} * -1px) calc({{animations[0].row}} * {{pixels}}* -1px);  
  }  
</style>

<!--- Embedded executable code--->  
<script>  
  ////////// convert yml hash to javascript key value objects /////////  
  var mario_metadata = {}; //key, value object  
  {% for key in hash %}  
    var key = "{{key | first}}"  //key  
    var values = {} //values object  
    values["row"] = {{key.row}}  
    values["col"] = {{key.col}}  
    values["frames"] = {{key.frames}}  
    mario_metadata[key] = values; //key with values added  
  {% endfor %}

  ////////// animation control object /////////  
  class Mario {  
    constructor(meta_data) {  
      this.tID = null;  //capture setInterval() task ID  
      this.positionX = 0;  // current position of sprite in X direction  
      this.currentSpeed = 0;  
      this.marioElement = document.getElementById("mario"); //HTML element of sprite  
      this.pixels = {{pixels}}; //pixel offset of images in the sprite, set by liquid constant  
      this.interval = 100; //animation time interval  
      this.obj = meta_data;  
      this.marioElement.style.position = "absolute";  
    }  

    animate(obj, speed) {  
      let frame = 0;  
      const row = obj.row * this.pixels;  
      this.currentSpeed = speed;  

      this.tID = setInterval(() => {  
        const col = (frame + obj.col) * this.pixels;  
        this.marioElement.style.backgroundPosition = `-${col}px -${row}px`;  
        this.marioElement.style.left = `${this.positionX}px`;  

        this.positionX += speed;  
        frame = (frame + 1) % obj.frames;  

        const viewportWidth = window.innerWidth;  
        if (this.positionX > viewportWidth - this.pixels) {  
          document.documentElement.scrollLeft = this.positionX - viewportWidth + this.pixels;  
        }  
      }, this.interval);  
    }  

    startWalking() {  
      this.stopAnimate();  
      this.animate(this.obj["Walk"], 3);  
    }  

    startRunning() {  
      this.stopAnimate();  
      this.animate(this.obj["Run1"], 6);  
    }  

    startPuffing() {  
      this.stopAnimate();  
      this.animate(this.obj["Puff"], 0);  
    }  

    startCheering() {  
      this.stopAnimate();  
      this.animate(this.obj["Cheer"], 0);  
    }  

    startFlipping() {  
      this.stopAnimate();  
      this.animate(this.obj["Flip"], 0);  
    }  

    startResting() {  
      this.stopAnimate();  
      this.animate(this.obj["Rest"], 0);  
    }  

    stopAnimate() {  
      clearInterval(this.tID);  
    }  
  }  

  const mario = new Mario(mario_metadata);  

  ////////// event control /////////  
  window.addEventListener("keydown", (event) => {  
    if (event.key === "ArrowRight") {  
      event.preventDefault();  
      if (event.repeat) {  
        mario.startCheering();  
      } else {  
        if (mario.currentSpeed === 0) {  
          mario.startWalking();  
        } else if (mario.currentSpeed === 3) {  
          mario.startRunning();  
        }  
      }  
    } else if (event.key === "ArrowLeft") {  
      event.preventDefault();  
      if (event.repeat) {  
        mario.stopAnimate();  
      } else {  
        mario.startPuffing();  
      }  
    }  
  });  

  //touch events that enable animations  
  window.addEventListener("touchstart", (event) => {  
    event.preventDefault(); // prevent default browser action  
    if (event.touches[0].clientX > window.innerWidth / 2) {  
      // move right  
      if (currentSpeed === 0) { // if at rest, go to walking  
        mario.startWalking();  
      } else if (currentSpeed === 3) { // if walking, go to running  
        mario.startRunning();  
      }  
    } else {  
      // move left  
      mario.startPuffing();  
    }  
  });  

  //stop animation on window blur  
  window.addEventListener("blur", () => {  
    mario.stopAnimate();  
  });  

  //start animation on window focus  
  window.addEventListener("focus", () => {  
     mario.startFlipping();  
  });  

  //start animation on page load or page refresh  
  document.addEventListener("DOMContentLoaded", () => {  
    // adjust sprite size for high pixel density devices  
    const scale = window.devicePixelRatio;  
    const sprite = document.querySelector(".sprite");  
    sprite.style.transform = `scale(${0.2 * scale})`;  
    mario.startResting();  
  });  

</script>


<script src="https://utteranc.es/client.js"
        repo="ZafeerA123/zafeer_2025"
        issue-term="title"
        label="blogpost-comment"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>