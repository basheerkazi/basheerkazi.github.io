---
lang: en
layout: page
title: Pichle tips
permalink: /tips/
description: Short, practical tips for parents and students on board exams, study habits and school choices.
---

Ek chhota tip roz. Yeh sab tips ek jagah par hain. Kisi tip ko apne parivaar ya class group mein bhejna ho toh neeche share button dabayein.

<ol class="tiplist">
{% for t in site.data.tips reversed %}
  <li>{{ t }}</li>
{% endfor %}
</ol>
