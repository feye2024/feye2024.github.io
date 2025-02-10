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

# 👨🏻‍🎓<font color="#4A708B">About Me</font>

I am currently pursuing a Ph.D. in Industrial and Systems Engineering and has obtained a M.Sc. in Statistics at Rutgers-New Brunswick <img src="./images/rutgers.png" style='width: 1.5em;'>. 

My research aims to advance the integration of physics, statistics, and modern AI/ML by constructing physics-guided data science models for improved renewable energy forecasting and operation. 

**Ph.D. Students Position Opening:** *I am actively* **looking for Ph.D. students** *starting in Fall 2025. Applicants with backgrounds in engineering, statistics, computer science, or related fields and strong coding skills are encouraged to apply. If interested, please email me your CV, transcript, and any additional materials that highlight your qualifications. Use **“Ph.D. Application – [Your Name]”** as the email subject. For more information, please check the Ph.D. programs in* [*IE*](https://www.clemson.edu/cecas/departments/ie/index.html)*.*

<span class='anchor' id='-news'></span>

# 🔥 <font color="#4A708B">News</font>
- *2025.01*: I will join [Clemson IE](https://www.clemson.edu/cecas/departments/ie/index.html) <img src="./images/clemson.png" style='width: 1.5em;'> as a tenure-track assistant professor!

<span class='anchor' id='-honors-and-awards'></span>

# 🏆 <font color="#4A708B">Honors and Awards</font>

- **First Place**, [IISE QCRE Track Best Student Poster Award](https://soe.rutgers.edu/news/ise-phd-student-wins-best-student-poster-competition-iise-annual-conference), *2024* 
- **First Place**, [IISE Energy Systems Track Best Paper Award](https://www.linkedin.com/posts/feng-y-51b3ba252_iiseannual2023-offshorewind-offshorewindenergy-activity-7067279451163611137-qNTu?utm_source=share&utm_medium=member_desktop), *2023* 
- **First Place**, [INFORMS Sustainability Cluster Best Student Paper Award](https://academicaffairs.rutgers.edu/njwind/fengye-wins-INFORMS-award), *2022* 
- New Jersey Wind Institute Fellowship (awarded to 10 graduate students in NJ per year), *2023*
- Rutgers Climate and Energy Institute (RCEI) Student Support Funding Award, *2024*
- Outstanding Ph.D. Student Award (Research), Department of Industrial & Systems Engineering , Rutgers University, *2024*
- Research & Travel Award, School of Graduate Studies, Rutgers University, *2024*
- Graduate Student Service Award, Department of Industrial & Systems Engineering, Rutgers University,  *2024*
- Rutgers University Fellowship, Department of Industrial & Systems Engineering, Rutgers University, *2024*

<span class='anchor' id='-publications'></span>

# 📝 <font color="#4A708B">Publications</font>
> (†: equal contribution, #: corresponding author)

## Research Paper
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">JAG</div><img src='../images/landsat.png' alt="sym" width="100%"></div></div>
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


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ESS</div><img src='images/ESS.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
 [PWV retrieval performance evaluation for the fresh BDS-3 with multi-source data](https://doi.org/10.1029/2023EA002923)

 Nan Jiang, Zhaorui Gao, **Yuhao Wu**, et al., 2023. *Earth and Space Science*. 10, e2023EA002923. (JCR Q2, IF=3.1). <br>
- From the tests applied with different satellite systems, we found that BDS-3 has a comparable PWV retrieval performance as global positioning system (GPS), and a better outcome was achieved using the combined data from GPS and BDS-3.
  

## Patent
- **F. Ye**, J. Brodie, T. Miles, and A. Ezzat, “Techniques to Provide Improved Wind Input for Operating Offshore Wind Turbines” (International Application #: PCT/US23/73816)
- Z. Zhang, **F. Ye**, C. Zhen and M. Dai, “Remote Data Acquisition and Analysis for Process Diagnosis in the Production Line” (in Chinese, Patent #: CN201810868396.X)


<span class='anchor' id='-invited-talks'></span>

# 💬 <font color="#4A708B">Invited/Conference Presentations</font>

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



<span class='anchor' id='-teaching'></span>

# 👨🏻‍🏫 <font color="#4A708B">Teaching/Mentoring</font>

- **Instructor** (with full responsibility) 06-07/2022, 2023

   Summer 440 EOF Matlab Computer Programming

- **Teaching Assistant** 01/2022 - 05/2022

  14:540:343: Engineering Economics

  14:540:462: Facilities Layout and Materials Handling

- **Student Mentoring**

  Master student researchers

  – Cory Petersen 09/2024 - present

  Topic: Accessibility Forecasting for Wind Farm Operations Considering Metocean Conditions

  – Xinxi “Chris” Zhang 09/2023 - 05/2024

  Topic: A Statistical Deep Learning Approach for Offshore Wind Energy Forecasting

  Undergraduate researchers

  – Prisha Bhamre (NSF REU) 09/2024 - present

  Topic: A Surrogate Model for Wind Farm Wake Effects

  – Briana Worrell (ARESTY) 09/2024 - present

  Topic: Digital Twins for Offshore Wind Farms

  – Jeeva Ramasamy (NJEDA OSW Fellowship Program) 09/2023 - present

  Topic: Data Science for Offshore Wind Energy Operations and Forecasting

  – Andrei Dimitriu (NJEDA OSW Fellowship Program) 08/2022 - 06/2023

  Topic: Data Analysis & Processing for the Offshore Wind Energy Areas in the Mid-Atlantic

  – Althea Miquela (NSF REU) 08/2022 - 06/2023

  Topic: Defect Detection in Solar Photovoltaic Systems Using UAVs and Machine Learning

  (Winner of the Student Paper Competition at the IEOM’s 8th North American Conference)



<span class='anchor' id='-service'></span>

#  <font color="#4A708B">Professional Service and Membership</font>

- **Vice President**: Rutgers INFORMS Student Chapter (Cum Laude Award) 10/2022 - present

- **Session chair**:

  “Predictive Analytics for Wind Power Generation”, IISE, Montreal, Canada, May 2024

  “Unique Directions in Energy Research”, IISE, Montreal, Canada, May 2024

  “Forecasting and Data Science for Renewable Energy”, INFORMS, Indianapolis, IN, Oct. 2022

- **Journal Reviewer for**:

  Technometrics, IISE Transactions, IEEE Transactions on Automation Science and Engineering, IEEE Transactions on Sustainable Energy, Renewable Energy, International Journal of Production Research, Applied Energy, INFORMS Journal on Data Science, Frontiers in Marine Science

  

  Memberships:
  • Institute of Industrial and Systems Engineers (IISE )
  • Institute for Operations Research and the Management Sciences (INFORMS )
  • Institute of Electrical and Electronics Engineers (IEEE )



<span class='anchor' id='-personal'></span>

# 🏃🏻 <font color="#4A708B">Personal</font>

## Photography

<div>
<img src="../images/photo1.jpg">
</div>

<font color="#ABABAB">The sunset outside the window of the tallest building at Shandong University (Weihai).</font><br>