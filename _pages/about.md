---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# 🙋‍♂️ <font color="#4A708B">About Me</font>

I am currently pursuing a Ph.D. in Industrial and Systems Engineering and has obtained a M.Sc. in Statistics at Rutgers-New Brunswick <img src="./images/rutgers.png" style='width: 1.5em;'>. 

My research aims to advance the integration of physics, statistics, and modern AI/ML by constructing physics-guided data science models for improved renewable energy forecasting and operation. 

**Ph.D. Students Position Opening:** *I am actively* **looking for Ph.D. students** *starting in Fall 2025. Applicants with backgrounds in engineering, statistics, computer science, or related fields and strong coding skills are encouraged to apply. If interested, please email me your CV, transcript, and any additional materials that highlight your qualifications. Use **“Ph.D. Application – [Your Name]”** as the email subject. For more information, please check the Ph.D. programs in* [*IE*](https://www.clemson.edu/cecas/departments/ie/index.html)*.*

<span class='anchor' id='-news'></span>

# 🔥 <font color="#4A708B">News</font>
- *2025.01*: I will join [Clemson IE](https://www.clemson.edu/cecas/departments/ie/index.html) <img src="./images/clemson.png" style='width: 1.5em;'> as a tenure-track assistant professor!

<span class='anchor' id='-honors-and-awards'></span>

# 🎖 Honors and Awards

- **First Place**, [IISE QCRE Track Best Student Poster Award](https://soe.rutgers.edu/news/ise-phd-student-wins-best-student-poster-competition-iise-annual-conference), *2024* 
- **First Place**, [IISE Energy Systems Track Best Paper Award](https://www.linkedin.com/posts/feng-y-51b3ba252_iiseannual2023-offshorewind-offshorewindenergy-activity-7067279451163611137-qNTu?utm_source=share&utm_medium=member_desktop), *2023* 
- **First Place**, [INFORMS Sustainability Cluster Best Student Paper Award](https://academicaffairs.rutgers.edu/njwind/fengye-wins-INFORMS-award), *2022* 
- New Jersey Wind Institute Fellowship (awarded to 10 graduate students in NJ per year), *2023*
- Rutgers Climate and Energy Institute (RCEI) Student Support Funding Award, *2024*
- Outstanding Ph.D. Student Award (Research), Department of Industrial & Systems Engineering , Rutgers University, *2024*
- Research & Travel Award, School of Graduate Studies, Rutgers University, *2024*
- Graduate Student Service Award, Department of Industrial & Systems Engineering, Rutgers University,  *2024*
- Rutgers University Fellowship, Department of Industrial & Systems Engineering, Rutgers University, *2024*



# 📝 <font color="#4A708B">Publications</font>
> (†: equal contribution, #: corresponding author)

## Research Paper
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">JAG</div><img src='images/landsat.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Improving the capability of water vapor retrieval from Landsat 8 using ensemble machine learning](https://doi.org/10.1016/j.jag.2023.103407)

**Yuhao Wu**, Nan Jiang, Yan Xu#, et al., 2023. *International Journal of Applied Earth Observation and Geoinformation*. 122, 103407. (JCR Q1, IF7.5).<br>

- The new method uses Gradient Boosting Decision Tree (GBDT) to establish the model between brightness temperature, GNSS-derived PWV, and related surface parameters. 
- Compared with SWCVR, the GBDT improves the RMSE and availability by 41.99% and 38.3%, respectively.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EJRS</div><img src='images/EJRS.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Revealing the water vapor transport during the Henan "7.20" heavy rainstorm based on ERA5 and real-time GNSS](https://doi.org/10.1016/j.ejrs.2024.02.004)

**Yuhao Wu**, Nan Jiang, Yan Xu#, et al., 2024. *Egyptian Journal of Remote Sensing and Space Sciences*. 27, 165-177. (JCR Q2, IF4.4).<br>
- Different from the normal rainfall, we found that the PWV variation during the Henan rainstorm experienced a unique "accumulation" period.
- In addition, the PWV in the severely damaged area was 20 mm higher than the average value of the past decade. Ten days after the rainstorm, the surface of this area had subsided by 1.5-3 mm.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">GRL</div><img src='images/GRL.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[First PWV Retrieval using MERSI-LL onboard FY-3E and Cross Validation with Co-platform Occultation and Ground GNSS](https://doi.org/10.1029/2024GL108681)

Nan Jiang†, **Yuhao Wu†**, Song Li, Yan Xu#, et al., 2024. *Geophysical Research Letters*. 51, e2024GL108681. (JCR Q1, IF=5.3).<br>
- Here, we carry out the PWV retrieval using the MERSI-LL sensor onboard the FY-3E satellite for the first time.
- For the results against ground-based GNSS, the total accuracy shows an RMSE of 2.69-3.36 mm as the clouds increase, and correlation coefficients higher than 0.95.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ESS</div><img src='images/ESS.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
 [PWV retrieval performance evaluation for the fresh BDS-3 with multi-source data](https://doi.org/10.1029/2023EA002923)

 Nan Jiang, Zhaorui Gao, **Yuhao Wu**, et al., 2023. *Earth and Space Science*. 10, e2023EA002923. (JCR Q2, IF=3.1). <br>
- From the tests applied with different satellite systems, we found that BDS-3 has a comparable PWV retrieval performance as global positioning system (GPS), and a better outcome was achieved using the combined data from GPS and BDS-3.
</div>
</div>

## Software Copyright
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">GPRA</div><img src='images/software1.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Batch retrieval software for water vapor based on Beidou/GNSS](https://b23.tv/1DP5ixu)

Yan Xu, **Yuhao Wu**, Nan Jiang, Tianhe Xu. 2022. 2023SR0222849.<br>
- Support reading of various raw ZTDs such as RTKLIB, Bernese, IGS, RPNT, etc.
- Quality control of raw ZTD based on dual median filtering algorithm.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">GWR</div><img src='images/software2.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[GNSS-SNR water level retrieval software](https://b23.tv/8GL6OGN)

**Yuhao Wu**, Dongliang Guan. 2021. 2021SR1211116.<br>
- Suitable for multiple systems such as BDS and GPS.
- Retrieval based on EMD algorithm.
</div>
</div>

## Patent
- Method and System for Monitoring Extraordinary Rainstorm on Basis of Multi-source Data. Nan Jiang, **Yuhao Wu**, Yan Xu, Tianhe Xu. 2023. Patent No.: US 11,852,779B1.<br>

## Degree Thesis

- **Master's thesis:** Research and Application of Water Vapor Retrieval by Integrating Ground-based GNSS and Spaceborne Thermal Infrared Remote Sensing Data. (Advisor: Dr. [Yan Xu](https://apd.wh.sdu.edu.cn/info/1510/1912.htm)). <br>

- **Bachelor's thesis:** Research on Water Level Change Monitoring Based on BeiDou Navigation Satellite System. (Advisor: Dr. [Dongliang Guan](https://cge.njtech.edu.cn/info/1045/2861.htm)). Excellent Graduation Thesis Award of Nanjing Tech University. First Prize for Outstanding Graduation Thesis of Undergraduate Geomatics Students in Jiangsu Province.<br>

# 💬 <font color="#4A708B">Invited Talks</font>

- **An Integro-Difference Equation Model for Spatio-Temporal Offshore Wind Forecasting**

  *IEEE Power & Energy Society General Meeting, Seattle, WA July 2024*
- **A Statistical Deep Learning Approach for Offshore Wind Energy Forecasting**

  *Rutgers Climate Symposium, New Brunswick, NJ Nov. 2024*

  *INFORMS Annual Meeting, Seattle, WA Oct. 2024*

  *IISE Annual Conference & Expo, Montreal, Canada May 2024*

- **AIRU-WRF: A Physics-guided Spatio-temporal Wind Forecasting Model and Its Application to the U.S. Mid Atlantic Offshore Wind Energy Areas**

  *NAWEA/WindTech 2024 Conference New Brunswick, NJ Oct. 2024*

  *New Jersey Offshore Wind Technology Conference, Newark, NJ Dec. 2023*

  *Rutgers Climate Symposium, New Brunswick, NJ Nov. 2023*

  *INFORMS Annual Meeting, Phoenix, AZ Oct. 2023*

  *Wind Institute Research Symposium, Trenton, NJ Apr. 2023*

  *INFORMS Annual Meeting, Indianapolis, IN Oct. 2022*

  *IISE Annual Conference & Expo, Seattle, WA May 2022*

- **Ultra-Short-Term Probabilistic Wind Forecasting: Can Numerical Weather Predictions Help?**

  *IEEE Power & Energy Society General Meeting, Orlando, FL July 2023*

  *IISE Annual Conference & Expo, New Orleans, LA May 2023*

# 💻 <font color="#4A708B">Teaching</font>
- From July 2018 to September 2018, I worked as a first grade homeroom teacher (volunteer teaching) at Hanwang Town Second Primary School in Mianzhu City, Sichuan Province, China.



<span class='anchor' id='-service'></span>

# 🔥 <font color="#4A708B">Service</font>

- *2025.01*: I will join [Clemson IE](https://www.clemson.edu/cecas/departments/ie/index.html) <img src="./images/clemson.png" style='width: 1.5em;'> as a tenure-track assistant professor!

  

<span class='anchor' id='-hobbies'></span>

# 📷 <font color="#4A708B">Hobbies</font>

## Photography

<div>
<img src="/images/photo1.jpg">
</div>
<font color="#ABABAB">The sunset outside the window of the tallest building at Shandong University (Weihai).</font><br>Photography opened the door to a new world for me: I began to observe the weather, the timing of the rise and fall of the sun and moon, the forecast of sunset, meteors, and the Milky Way. **To see the world, things dangerous to come to, to see behind walls, to draw closer, to find each other and to feel. That is the purpose of life.**<br>
<div>
<img src="/images/photo2.jpg">
</div>
<br>During my three years in Weihai, I took many meaningful photos and made some friends who took photos together. My camera is *Nikon Z50*, with lenses of *50-250 mm* and *16-50 mm*. In addition, I also have an *Olympus IS-5000* film camera. But in the past year, I have hardly touched them because I have devoted all my time to scientific research.<br>If you like the style of my photos, then we might be kindred spirits. More photos can be viewed on my [Little Red Book](https://www.xiaohongshu.com/user/profile/5b59dc27f7e8b977d3628016).

## Past Hobbies

<div>
<img src="/images/paint1.jpg">
</div>
<font color="#ABABAB">I drew it in high school.</font>
Before going to college, I was studying sketching and almost became an art student.

<span class='anchor' id='-visitor-map'></span>
# 🌏️ <font color="#4A708B">Visitor Map</font>

<script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=375e86&w=370&t=tt&d=6gCLp8H0jUJXTDAgwenOxbDgCEaAvQc8Hgj55t1cF1k&co=9ecdee&cmo=ffbdf7&cmn=fffc2e&ct=000000'></script>