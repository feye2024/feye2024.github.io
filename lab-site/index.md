---
layout: default
---

<section id="home" class="lab-intro" aria-label="Home">
  <div class="earth-hero">
    <img src="{{ '/images/earth_text.gif' | relative_url }}" width="1920" height="1080" alt="Animated view of Earth from space" loading="eager" fetchpriority="high">
  </div>
  <div class="lab-intro-copy">
    {% capture home_intro %}{% include home-intro.md %}{% endcapture %}
    {{ home_intro | markdownify }}
  </div>
</section>


<section id="people" aria-labelledby="people-title">
  <h2 id="people-title">People</h2>
  <div class="people-group" aria-labelledby="director-title">
    <h3 id="director-title" class="group-title">Principal Investigator and Lab Director</h3>
    <div class="person">
      <img src="{{ '/assets/images/feng-ye.jpg' | relative_url }}" alt="Feng Ye">
      <div>
        <h4>Feng Ye</h4>
        <p class="role">Assistant Professor</p>
        <p><a href="https://feye2024.github.io/">Personal Website</a></p>
      </div>
    </div>
  </div>
  <div class="people-group" aria-labelledby="members-title">
    <h3 id="members-title" class="group-title">Member</h3>
    <ul class="members-list">
      <li>
        <img class="member-photo" src="{{ '/images/sitong.PNG' | relative_url }}" width="1086" height="1448" alt="Si-Tong Yang" loading="lazy" decoding="async">
        <h4>Si-Tong Yang</h4>
        <p class="role">Ph.D. Student<br>(Spring 2026–now)</p>
      </li>
      <li>
        <img class="member-photo" src="{{ '/images/xuanhechen.png' | relative_url }}" width="1086" height="1145" alt="Xuanhe Chen" loading="lazy" decoding="async">
        <h4>Xuanhe Chen</h4>
        <p class="role">Ph.D. Student<br>(Fall 2026–now)</p>
      </li>
    </ul>
  </div>
  <div class="people-group" aria-labelledby="alumni-title">
    <h3 id="alumni-title" class="group-title">Alumni</h3>
    <ul class="alumni-list">
      <li><strong>Cory Petersen</strong> — <span class="role">M.S. Student</span> <span class="dates">(2024–2025)</span></li>
      <li><strong>Xinxi “Chris” Zhang</strong> — <span class="role">M.S. Student</span> <span class="dates">(2023–2024)</span></li>
      <li><strong>Prisha Bhamre</strong> — <span class="role">Undergraduate Student</span> <span class="dates">(2024–2025)</span></li>
      <li><strong>Briana Worrell</strong> — <span class="role">Undergraduate Student</span> <span class="dates">(2024–2025)</span></li>
      <li><strong>Jeeva Ramasamy</strong> — <span class="role">Undergraduate Student</span> <span class="dates">(2023–2025)</span></li>
      <li><strong>Andrei Dimitriu</strong> — <span class="role">Undergraduate Student</span> <span class="dates">(2022–2023)</span></li>
      <li><strong>Althea Miquela</strong> — <span class="role">Undergraduate Student</span> <span class="dates">(2022–2023)</span></li>
    </ul>
  </div>
</section>


<section id="publications" aria-labelledby="publications-title" markdown="1">
## Publications
{: #publications-title }

Selected publications on spatiotemporal learning and forecasting for weather and energy systems.

{% include publications.md %}
</section>


<section id="opening" aria-labelledby="opening-title" markdown="1">
## Opening
{: #opening-title }

### Ph.D. Student Openings

I am always looking for excellent students with high motivation and strong research potential to join our lab.

Applicants with backgrounds in engineering, statistics, computer science, or related fields and strong coding skills are encouraged to apply. If interested, please email me your CV, transcript, and any additional materials that highlight your qualifications to [fengye.recruit@gmail.com](mailto:fengye.recruit@gmail.com). Use **“Ph.D. Application – Your Name – Target Term”** as the email subject. For more information, please check the Ph.D. programs at [Clemson IE](https://www.clemson.edu/cecas/departments/ie/index.html).
</section>
