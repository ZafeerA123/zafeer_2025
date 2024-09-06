---
layout: base
title: Student Home 
description: Home Page
hide: true
---

<table cellpadding="10">
    <tr>
        <td><a href="{{site.baseurl}}/ToolsJourney">Tools Journey</a></td>
        <td><a href="{{site.baseurl}}/snake">Previous Website</a></td>
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
        background-color: #4CAF50; /* Green */
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
        transition: background-color 0.3s ease;
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

      /* Bordered div boxes */
      .bordered-box {
        border: 2px solid orange; /* Change border to orange */
        padding: 20px;
        margin-top: 10px;
      }
    </style>
</head>
<body>

    <!-- Paragraph element -->
    <p>This is a paragraph.</p>

    <!-- First div box with gradient button -->
    <div class="bordered-box">
      Click this button !
      <button class="gradient-button">Button</button>
    </div>

    <!-- Second div box for the 'Past Projects' button with same styling -->
    <div class="bordered-box">
      <button class="gradient-button" onclick="window.open('https://zafeera123.github.io/Personal2/', '_blank')">Past Projects</button>
    </div>

</body>
</html>

<br> 

## Introduction

My name is Zafeer Ahmed. I am a junior at DNHS, and currently enrolled in:

<ul>
  <li class="fade-in">AP Physics</li>
  <li class="fade-in" style="animation-delay: 0.5s;">AP Calculus AB</li>
  <li class="fade-in" style="animation-delay: 1s;">AP English</li>
  <li class="fade-in" style="animation-delay: 1.5s;">AP Computer Science Principles</li>
  <li class="fade-in" style="animation-delay: 1.5s;">Spanish 6</li>
</ul>

## Why did I take this class?

I took this class because I am very passionate about the field of computer science. Also, last year, I had taken the prerequisite to this class, CSSE 1-2. CSSE 1-2 really prepared me for this class, as it allowed me to complete most of the Tool Setups on the first day. Here is a link to my previous home page where all of my past projects are:

<!-- The 'Past Projects' button has already been moved below -->

## My Future Goals

After completing high school, I plan to go into some field of Engineering or Medicine. I'm passionate about technology and innovation, and I really hope to make a difference.
