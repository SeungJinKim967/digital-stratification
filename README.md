# Digital Stratification: Quantifying Educational Apartheid in the Global Knowledge Economy

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Research Status](https://img.shields.io/badge/status-submitted%20to%20Nature-green.svg)](https://github.com/SeungJinKim967/digital-stratification)

## Overview

This repository contains the complete computational framework for reproducing results from our Nature Human Behaviour manuscript: **"Digital education creates algorithmic apartheid between civilizations"**.

**Key Findings:**
- Educational systems worldwide create "algorithmic apartheid" through systematic cognitive separation
- Asia's extreme STEM emphasis (Balance Index 0.162) vs Europe's balanced approach (0.457) 
- Strong correlations with democratic capacity (r=0.689) and innovation outcomes (r=0.847)
- Policy simulations show 182% improvement potential through educational rebalancing

## Research Impact

Our novel **Balance Index** provides the first standardized international metric for educational equilibrium:

Balance Index = min(STEM%, Humanities%) / max(STEM%, Humanities%)
This framework enables evidence-based educational policy targeting and international comparison.

## Repository Structure
digital-stratification/
├── data/                                 # Research datasets
│   ├── balance_index_47_countries.csv   # Main analysis dataset (47 countries)
│   └── time_series_data.csv            # Temporal trends (2015-2024)
├── analysis/                            # Analysis code
│   ├── statistical_analysis.py         # Complete statistical reproduction
│   ├── generate_figures.py             # Publication-quality figures
│   └── reproduce_results.py            # One-click reproduction script
├── figures/                             # Generated manuscript figures
├── results/                             # Statistical outputs and reports
├── requirements.txt                     # Python dependencies
├── LICENSE                             # MIT License
└── README.md                           # This file

## Quick Start (For Nature Reviewers)

**Complete reproduction in 3 commands:**

```bash
# 1. Clone repository
git clone https://github.com/SeungJinKim967/digital-stratification.git
cd digital-stratification

# 2. Install dependencies
pip install -r requirements.txt

# 3. Reproduce ALL results
cd analysis
python reproduce_results.py

Expected output:

All manuscript statistics reproduced
5 publication-quality figures generated
Complete validation report
Runtime: 2-3 minutes

Detailed Installation
Prerequisites

Python 3.8 or higher
Git

Step-by-step Setup

Clone the repository:
git clone https://github.com/SeungJinKim967/digital-stratification.git
cd digital-stratification
Create virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Verify installation:
cd analysis
python -c "import pandas, numpy, scipy, matplotlib, seaborn; print('All dependencies installed successfully')"
Usage Instructions
Option 1: Complete Reproduction (Recommended)
cd analysis
python reproduce_results.py
This generates:

All statistical results validation
All 5 manuscript figures
Supplementary materials
Comprehensive reproduction report

Option 2: Individual Components
Statistical Analysis:
cd analysis
python statistical_analysis.py
Figure Generation:
cd analysis
python generate_figures.py
Balance Index Calculator:
cd analysis
python -c "
from statistical_analysis import DigitalStratificationAnalysis
analyzer = DigitalStratificationAnalysis()
print(f'Asia Balance Index: {analyzer.main_data[analyzer.main_data[\"region\"]==\"Asia\"][\"balance_index\"].mean():.3f}')
"
Key Results Reproduction
Manuscript Table 1: Continental Patterns
from analysis.statistical_analysis import DigitalStratificationAnalysis

analyzer = DigitalStratificationAnalysis()
regional_stats = analyzer.descriptive_statistics()

Manuscript Table 2: Correlation Analysis
correlations = analyzer.correlation_analysis()
# Democratic Participation: r=0.689, p<0.01
# Innovation Capacity: r=0.847, p<0.001

Manuscript Figures 1-5
from analysis.generate_figures import FigureGenerator

fig_gen = FigureGenerator()
fig_gen.generate_all_figures()

Data Description
Main Dataset (balance_index_47_countries.csv)

Countries: 47 nations across 5 continental regions
Key Variables:

balance_index: Educational equilibrium measure (0-1)
stem_percent: STEM graduates percentage
humanities_percent: Humanities graduates percentage
democratic_participation_index: Democratic capacity measure
innovation_capacity_index: Innovation outcomes measure



Time Series Dataset (time_series_data.csv)

Coverage: 2015-2024 annual data
Countries: All 47 nations
Purpose: Temporal trend analysis and policy impact assessment

Methodology
Balance Index Calculation
The Balance Index quantifies educational equilibrium using the ratio of minimum to maximum percentages between STEM and humanities education:
def calculate_balance_index(stem_percent, humanities_percent):
    return min(stem_percent, humanities_percent) / max(stem_percent, humanities_percent)
Statistical Framework

Correlation Analysis: Pearson correlations with democratic and innovation outcomes
ANOVA: Regional differences testing (F=127.3, p<0.001, η²=0.924)
Time Series: Linear regression for trend analysis (2015-2024)
Effect Sizes: Cohen's d and eta-squared for practical significance

Policy Simulation
Monte Carlo analysis (10,000 iterations) modeling European Integration Model adoption:

Investment requirements: €18.5B over 10-15 years for Asia
Expected improvement: 182% Balance Index increase
Implementation timeline: 3-6-10 year milestones

Results Summary
Regional Patterns
RegionSTEM %Humanities %Balance IndexClassificationAsia44.67.20.162CrisisEurope33.915.60.461SustainableNorth America29.711.40.385CautionDeveloping Countries25.313.20.523Apparent Balance*Africa20.411.30.556Constrained Balance*
*Resource-constrained rather than intentional balance
Key Correlations

Democratic Participation: r=0.689, p<0.01
Innovation Capacity: r=0.847, p<0.001
Civic Engagement: r=0.723, p<0.001
Social Trust: r=0.534, p<0.05

Digital Stratification Ratio
2.90:1 - STEM gaps exceed humanities gaps by nearly threefold globally, indicating systematic rather than random educational inequality.
Troubleshooting
Common Issues

1. Import errors:
# Ensure you're in the analysis directory
cd analysis
python reproduce_results.py
2. Missing dependencies:
pip install --upgrade pandas numpy scipy matplotlib seaborn scikit-learn plotly
3. Data file not found:
# Verify data files exist
ls ../data/
# Should show: balance_index_47_countries.csv, time_series_data.csv
4. Figure generation fails:
# Create figures directory
mkdir -p ../figures
cd analysis
python generate_figures.py
System Requirements

RAM: Minimum 4GB (8GB recommended)
Storage: 500MB free space
Python: 3.8+ (tested on 3.8, 3.9, 3.10, 3.11)
OS: Windows 10+, macOS 10.14+, Ubuntu 18.04+

Citation
If you use this research or codebase, please cite:
@article{kim2024digital,
  title={Digital education creates algorithmic apartheid between civilizations},
  author={Kim, Seung Jin},
  journal={Nature Human Behaviour},
  year={2024},
  note={Under review}
}

License
This project is licensed under the MIT License - see the LICENSE file for details.
Contributing
We welcome contributions to improve the analysis framework:

Fork the repository
Create a feature branch (git checkout -b feature/improvement)
Commit changes (git commit -am 'Add new analysis')
Push to branch (git push origin feature/improvement)
Create Pull Request

Contact
Corresponding Author: Seung Jin Kim
Email: seungjin.kim@[institution].edu
ORCID: 0000-0000-0000-0000
Repository: https://github.com/SeungJinKim967/digital-stratification
Issues: https://github.com/SeungJinKim967/digital-stratification/issues
Acknowledgments

UNESCO Institute for Statistics for educational data access
OECD Education Directorate for international statistics
Digital Innovation Institute for computational resources
Regional education specialists for data validation

Version History

v1.0.0 - Initial submission to Nature Human Behaviour
v0.9.0 - Complete reproducibility framework
v0.8.0 - Statistical analysis finalization
v0.7.0 - Data validation and cleaning
v0.6.0 - Balance Index development and testing
