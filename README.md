# Digital Stratification Research Repository

> **Quantifying Educational Apartheid in the Global Knowledge Economy**
> 
> 🎯 Research examining STEM vs Humanities education patterns across 47 countries
> 
> 📊 **Balance Index**: Novel metric for educational equilibrium measurement
> 
> [![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)

---

## 📋 Quick Start

### Installation
```bash
git clone https://github.com/SeungJinKim967/digital-stratification.git
cd digital-stratification
pip install -r requirements.txt
Core Analysis
from analysis.balance_calculator import BalanceIndex

# Calculate Balance Index for any country
balance = BalanceIndex(stem_percent=43.9, humanities_percent=7.1)
print(f"Asia Balance Index: {balance.calculate():.3f}")  # 0.162
 Key Findings
RegionSTEM %Humanities %Balance IndexRatioAsia43.9%7.1%0.1626.2:1Europe33.9%15.5%0.4572.2:1North America29.9%11.2%0.3752.7:1Developing24.3%13.0%0.5351.9:1Africa19.5%11.4%0.5851.7:1
🔥 Digital Stratification Ratio: 2.90:1 (STEM gaps exceed humanities gaps by ~3x)
 Research Overview
The global knowledge economy has created a new form of educational segregation: "digital stratification"—the systematic divergence between STEM and humanities education across continental regions.
Key Contributions

Balance Index: Novel metric quantifying educational equilibrium (0-1 scale)
Digital Stratification Ratio: Measures systematic educational inequality globally
European Integration Model: Policy simulation framework for educational reform
47-Country Analysis: Comprehensive dataset spanning 5 continental regions

Critical Findings

Educational Apartheid: Asia exhibits extreme imbalance (Balance Index 0.162)
Democratic Implications: Regions with low balance may face governance challenges
Policy Solutions: European Integration Model could improve Asia's balance by 182%
 Repository Contents
digital-stratification/
├── 📊 data/                     # Research datasets
│   └── README.md               # Data documentation
├── 🔬 analysis/                 # Core calculation modules
│   └── balance_calculator.py   # Balance Index computation
├── 📄 requirements.txt         # Python dependencies
└── 📋 README.md               # This file
🧮 Balance Index Calculator
Core Metric
def balance_index(stem_percent, humanities_percent):
    """Calculate educational equilibrium."""
    return min(stem_percent, humanities_percent) / max(stem_percent, humanities_percent)
Interpretation Scale

0.8-1.0: 🟢 Excellent Balance
0.6-0.8: 🟡 Good Balance
0.4-0.6: 🟠 Moderate Imbalance
0.2-0.4: 🔴 Severe Imbalance
0.0-0.2: ⚫ Critical Imbalance (Educational Apartheid)
📈 Usage Examples
Quick Analysis
from analysis.balance_calculator import BalanceIndex

# Asia analysis
asia = BalanceIndex(43.9, 7.1, region="Asia")
print(asia.interpretation())

# Europe analysis  
europe = BalanceIndex(33.9, 15.5, region="Europe")
print(europe.interpretation())
📖 Academic Citation
@article{digital_stratification_2025,
    title={Digital Stratification: The Emergence of Educational Apartheid in the Global Knowledge Economy},
    author={Kim, SeungJin and Research Team},
    journal={Nature Human Behaviour},
    year={2025},
    note={Data and code: https://github.com/SeungJinKim967/digital-stratification}
}
🌍 Data Sources

UNESCO Global Education Database (2020-2024)
OECD Education Statistics
National Ministry Reports (47 countries)

Coverage: 635,316 graduate enrollments across 5 continental regions
📞 Contact

Lead Researcher: SeungJinKim967
Repository: GitHub Issues


📄 License
This project is licensed under the MIT License.

🌟 Star this repository if you find it useful for educational research!
