---
layout: page 
title: Soccer
permalink: /soccer/
---
 <!-- Soccer Club Section -->
<section id="soccer-clubs">
  <h1>My Favorite Soccer Clubs</h1>
  
  <!-- Barcelona Club -->
  <div id="barcelona">
    <h2>FC Barcelona</h2>
    <img src="{{site.baseurl}}/images/barca.png" alt="Barcelona FC" style="width: 300px;">
    <p>FC Barcelona, also known as Barça, is a professional football club based in Barcelona, Spain. Known for their iconic blue and garnet kit, Barcelona has a rich history and is one of the most successful clubs in the world.</p>
  </div>
  
  <hr>

  <!-- Argentina FC -->
  <div id="argentina-fc">
    <h2>Argentina FC</h2>
    <img src="{{site.baseurl}}/images/argentina.jpg" alt="Argentina FC" style="width: 300px;">
    <p>Argentina's national football team, winners of multiple World Cups, is famous for its outstanding players like Diego Maradona and Lionel Messi. Their iconic sky-blue and white striped kit represents one of the most passionate football nations in the world.</p>
  </div>
</section>

<hr>

<!-- Cool Interactive Soccer Feature -->
<section id="cool-feature">
  <h2>Interactive Soccer Ball!</h2>
  <p>Move your mouse and watch the soccer ball follow!</p>

  <!-- Soccer Ball Animation -->
  <div id="soccer-ball-container">
    <img src="{{site.baseurl}}/images/soccer-ball.png" id="soccer-ball" alt="Soccer Ball" style="position: absolute; width: 80px; top: 50px; left: 50px;">
  </div>
</section>

<!-- Add Custom CSS for Styling -->
<style>
  /* General Styles */
  #soccer-clubs {
    text-align: center;
    font-family: Arial, sans-serif;
  }

  #soccer-clubs img {
    border-radius: 15px;
    margin-top: 10px;
  }

  #cool-feature {
    text-align: center;
    margin-top: 40px;
    font-family: Arial, sans-serif;
  }

  /* Soccer Ball Animation */
  #soccer-ball-container {
    height: 300px;
    position: relative;
  }

  #soccer-ball {
    transition: transform 0.1s linear;
  }
</style>

<!-- Add JavaScript for Soccer Ball Animation -->
<script>
  const soccerBall = document.getElementById('soccer-ball');

  // Event listener to track mouse movement
  document.addEventListener('mousemove', function(event) {
    const x = event.clientX - 40; // Offset by half the ball's width
    const y = event.clientY - 40; // Offset by half the ball's height

    // Move the soccer ball to follow the mouse
    soccerBall.style.transform = `translate(${x}px, ${y}px)`;
  });
</script>

 <script src="https://utteranc.es/client.js"
        repo="nighthawkcoders/zafeer_2025"
        issue-term="title"
        label="blogpost-comment"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>