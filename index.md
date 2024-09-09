---
layout: base
title: Student Home 
description: Home Page
hide: true
image: /images/mario_animation.png
---

<table cellpadding="10">
    <tr>
        <td><a href="{{site.baseurl}}/ToolsJourney">Tools Journey</a></td>
        <td><a href="{{site.baseurl}}/Sprint1TSDP">Sprint 1 Partner Check</a></td>
    </tr>
</table>

<div style="align-items: center; display: flex; flex-direction: column;">
    <a href="{{site.baseurl}}/">
        <img src="{{site.baseurl}}/images/globe.gif" height="60" title="Globe [:" alt="" style="margin-top: -140px; margin-left: 880px;">
    </a>
</div>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Home</title>
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
    </style>
</head>
<body>

    <!-- Paragraph element -->
    <p>This is a paragraph.</p>

    <!-- First div with the gradient button -->
    <div class="transparent-box">
        Click this button!
        <button class="gradient-button">Button</button>
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

  /*CSS style rules for the elements id and class above...
  */
  .sprite {
    height: {{pixels}}px;
    width: {{pixels}}px;
    background-image: url('{{sprite_file}}');
    background-repeat: no-repeat;
  }

  /*background position of sprite element
  */
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

