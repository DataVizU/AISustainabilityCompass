![header](https://unstats.un.org/bigdata/events/2023/un-datathon/banner.jpg)

# AI Sustainability Compass
  Optimizing Local Solutions for the Sustainable Application of Large Language Models in China's Provinces
  
## Team Green & Long          
  Jingyi Li: ruclijingyi@foxmail.com
  
  Qianhe Chen: qianhechen01@gmail.com (https://github.com/chenqianhe)
  
  Yuetong Liu: liuyuetong@phoehub.net
  
  Jun Liu: junl5@illinois.edu
  
  Dai Yu: daiyu@phoehub.net

## Objectives
AI could stand as a fundamental pivot, yet an initial compass would be the primary step.

## Solution
1. Readiness Assessment: Evaluate a region's preparation level to embrace AI advancements.
2. Deployment Forecasting: Solution Optimization by Tailor LLM applications for regional decision-makers, enhancing local solutions


## Readiness Assessment:
Regional macro-model readiness rating based on the fuzzy comprehensive evaluation method.

6 Dimensions: Economy, People, Environment, Risks, Government, Infrastructure

Result:
We used geoinfo components to analyze and visualize our evaluation results.
<img width="1300" alt="image" src="https://github.com/mc856/readmetest/assets/39075334/7ed9d390-f385-4b74-9b27-e4c9ad783171">

### Assessment Criteria
#### 1.Economy
Stage 1: Per capita GDP and the level of digital economy development are below the national or reference regional average, with a weak industrial and service sector base.

Stage 2: Per capita GDP or digital economy development level is close to the national average, with a small number of AI enterprises.

Stage 3: Both GDP and digital economy development levels are above the national average, with a certain number of AI enterprises.

Stage 4: Both GDP and digital economy development levels are among the top in the nation, with a large number of AI enterprises.

Stage 5: Both GDP and digital economy development levels are at the forefront internationally, with numerous AI enterprises including leading companies.

#### 2.Government
Stage 1: Government expenditure on science and technology is a very low proportion of fiscal spending, with few AI policies of poor quality and inadequate implementation.

Stage 2: Limited government expenditure on science and technology with a growing trend, few AI policies, and implementation needs to be strengthened.

Stage 3: Government science and technology expenditure is a significant proportion, with a moderate number of AI policies of good quality and gradually strengthening implementation.

Stage 4: High proportion of government expenditure on science and technology, significant investment in the AI field, many AI policies of high quality, and strong implementation.

Stage 5: Government investment in the AI field reaches advanced international levels, with numerous high-quality AI policies, strong implementation, and a mechanism for continuous updates and improvements.

#### 3.Infrastructure
Stage 1: Low internet access ratio, indicating insufficient mobile network coverage, and an electrical grid that cannot support the power demands of large-scale industry or high-tech enterprises.

Stage 2: Increasing internet access ratio, showing some improvement in mobile networks; increased total power generation, but possibly still insufficient to attract large energy-consuming enterprises.

Stage 3: Maturing network infrastructure with good electricity support capabilities, able to adequately support the AI industry.

Stage 4: High internet access ratio, capable of supporting energy-intensive industries and technology enterprises.

Stage 5: Very high internet access ratio, providing very attractive economic conditions, conducive to attracting global AI enterprises and investment.

#### 4.People
Stage 1: The majority of the employed population has a low level of education, with a high proportion of primary education or less, and few with higher education.

Stage 2: A certain proportion of the employed population has completed basic education, with more than 40% having primary education, but still lacking in secondary and higher education talent.

Stage 3: A higher proportion of the employed have junior high education, with a certain percentage of technical and professional talent.

Stage 4: The proportion of employed with high school education reaches over 40%, and the number of higher education talents starts to increase.

Stage 5: The proportion of employed with at least a college education reaches over 40%, with a large number of highly skilled talents and research personnel.

#### 5.Environment
Stage 1: Possibility of extreme high temperatures, severe shortage of water resources, unable to meet the water demand of large-scale industrial use.

Stage 2: Higher temperatures, limited water resources, though able to support certain scales of industrial activities, still face challenges.

Stage 3: Moderate temperatures, a moderate share of industrial water use, capable of supporting the further development of the AI industry.

Stage 4: Cooler temperatures, abundant water resources, highly suitable for building large-scale data centers and computing facilities.

Stage 5: Low temperatures, very abundant water resources, mature and highly developed industrial base, efficient water resource management capability, able to support various industrial activities including AI without stress.


#### 6.Risk
Stage 1: High social security issues and economic instability, low technological acceptance.

Stage 2: Social issues with AI crimes still prominent, overall poor employment situation.

Stage 3: Good social stability, unemployment rates within controllable limits, balanced societal views on AI.

Stage 4: Good acceptance of AI technology in the region, good security conditions, relatively stable economy, low unemployment rates.

Stage 5: Very positive societal attitude towards AI, excellent security conditions, very low crime rates, extremely stable economic conditions. Unemployment rates are very low, the job market is very active, especially in the AI industry. There is a high degree of technological acceptance, as well as solid investment and educational foundations, providing fertile ground for the flourishing development of the AI industry.


## Deployment Forecasting

### Step 1: Assessing the Efficacy of Different LLMs
We cited the test results from Hugging Face to assess the effects and efficiency of different LLMs. The effectiveness includes four assessments: AI large model inference capability assessment (ARC), common sense reasoning assessment (HellaSwag), comprehension ability assessment (MMLU), and correctness assessment (TruthfulQA). The efficiency is based on LLM's memory requirements, inference speed, and energy demands.

### Step 2: Assessing the Efficacy of Different LLMs in Various Locations/Scales
The Impact of LLMs on the Economy


![image](https://github.com/mc856/readmetest/assets/39075334/d1b91158-0c29-47f1-ac7b-16dbf32d1cce)


Y represents total social output, represented by GDP.

A is total factor productivity, estimated from 2000-2019 data based on empirical model research. H is the employment in high-tech positions, represented by the number of people with at least an undergraduate degree.

K is the employment displaced by LLMs.

L is the employment in low-tech positions, represented by the number of people with below an undergraduate degree.

α, η are output elasticities, estimated to be based on empirical research in artificial intelligence.
 

## Future
#### 1. Immediate Impact
Our goal is for our product to give regions a real-time snapshot of where they stand in the large language model landscape, clue them in on their next moves, and guide them towards a suitable development path.
#### 2. Expansion Horizon
As AI's large language models keep growing and diversifying, we're keen to assess a broader array of models. The trustworthiness of these AI behemoths is a bit of a blind spot right now due to a lack of data for assessment, which we're looking to shore up going forward. Our plan is to take this system global, spicing things up with new parameters tailored to each country's unique profile.
#### 3. Diverse Talent Magnet
This project has really opened our eyes to the magic of teaming up across disciplines. We're on the hunt for team members from different backgrounds to sparkle to our work. For example, a designer not only helps beautify the pages but can also offers fresh perspectives on the analytical framework and content structure from a design standpoint.


## Appendix
### Data
National Bureau of Statistics, Provincial Statistical Bureaus:
    * GDP, per capita GDP, permanent population, scale of the digital industry, internet broadband access users, mobile internet users, total electricity generation, total water resources, per capita water resources, water supply volume, industrial water use volume, urban registered unemployment rate, government general public budget expenditure
    Website: https://data.stats.gov.cn/
    
Provincial Power Grid Companies:
    * Industrial electricity prices
    
China Labor Statistical Yearbook:
    * Distribution of educational levels among the employed population
    
China Law Yearbook:
    * Crime rate
    
European Centre for Medium-Range Weather Forecasts:
    * ERA5-Land monthly average temperature data
    https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land-monthly-means?tab=overview
    
PKULAW:
    * Artificial intelligence policies 
    https://www.pkulaw.com/
    
Qichacha:
    * Number of artificial intelligence companies 
    https://www.qcc.com/

WiSKY:
    * Sentiment tendency of public opinion news 
     https://wisky.wengegroup.com/

  
### Project Demo

https://ai-sustainability-compass.datavizu.app/

https://ai-sustainability-compass.datavizu.app/zh

