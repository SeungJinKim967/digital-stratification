"""
Digital Stratification: Balance Index Calculator
============================================

Core module for calculating educational balance metrics.
Implements the novel Balance Index and Digital Stratification Ratio.

Author: Digital Stratification Research Team
License: MIT
"""

import math

class BalanceIndex:
    """
    Calculate and analyze educational balance using the Balance Index metric.
    
    The Balance Index quantifies educational equilibrium between STEM and 
    humanities education, ranging from 0 (complete imbalance) to 1 (perfect balance).
    
    Formula: Balance Index = min(STEM%, Humanities%) / max(STEM%, Humanities%)
    """
    
    def __init__(self, stem_percent, humanities_percent, region=None):
        """
        Initialize Balance Index calculator.
        
        Args:
            stem_percent: Percentage of students in STEM fields (0-100)
            humanities_percent: Percentage of students in humanities fields (0-100)
            region: Optional region identifier
        """
        self.stem_percent = self._validate_percentage(stem_percent, "STEM")
        self.humanities_percent = self._validate_percentage(humanities_percent, "Humanities")
        self.region = region
        
    def _validate_percentage(self, value, field_name):
        """Validate percentage input."""
        if not 0 <= value <= 100:
            raise ValueError(f"{field_name} percentage must be between 0 and 100")
        return value
    
    def calculate(self):
        """
        Calculate the Balance Index.
        
        Returns:
            float: Balance Index value (0-1)
        """
        if self.stem_percent == 0 and self.humanities_percent == 0:
            return 0.0
            
        max_pct = max(self.stem_percent, self.humanities_percent)
        min_pct = min(self.stem_percent, self.humanities_percent)
        
        return min_pct / max_pct if max_pct > 0 else 0.0
    
    def ratio(self):
        """
        Calculate STEM:Humanities ratio.
        
        Returns:
            float: Ratio of STEM to humanities percentages
        """
        if self.humanities_percent == 0:
            return float('inf') if self.stem_percent > 0 else float('nan')
        return self.stem_percent / self.humanities_percent
    
    def interpretation(self):
        """
        Provide interpretation of Balance Index score.
        
        Returns:
            dict: Interpretation categories and recommendations
        """
        balance_score = self.calculate()
        ratio_score = self.ratio()
        
        if balance_score >= 0.8:
            category = "Excellent Balance"
            interpretation = "Near-optimal educational equilibrium"
            recommendation = "Maintain current balance while monitoring trends"
        elif balance_score >= 0.6:
            category = "Good Balance"
            interpretation = "Reasonable educational balance with room for improvement"
            recommendation = "Minor adjustments to achieve optimal balance"
        elif balance_score >= 0.4:
            category = "Moderate Imbalance"
            interpretation = "Significant educational stratification present"
            recommendation = "Systematic policy intervention needed"
        elif balance_score >= 0.2:
            category = "Severe Imbalance"
            interpretation = "Extreme educational stratification"
            recommendation = "Urgent comprehensive reform required"
        else:
            category = "Critical Imbalance"
            interpretation = "Educational apartheid conditions"
            recommendation = "Emergency intervention and complete restructuring needed"
            
        return {
            'balance_index': balance_score,
            'stem_humanities_ratio': ratio_score,
            'category': category,
            'interpretation': interpretation,
            'recommendation': recommendation
        }

# Quick calculation function
def calculate_balance_index(stem_percent, humanities_percent):
    """
    Quick Balance Index calculation.
    
    Args:
        stem_percent: STEM field percentage
        humanities_percent: Humanities field percentage
        
    Returns:
        float: Balance Index (0-1)
    """
    calculator = BalanceIndex(stem_percent, humanities_percent)
    return calculator.calculate()

# Example usage
if __name__ == "__main__":
    # Example: Asia region analysis
    asia_balance = BalanceIndex(43.9, 7.1, region="Asia")
    print(f"Asia Balance Index: {asia_balance.calculate():.3f}")
    print(f"Asia Interpretation: {asia_balance.interpretation()}")
    
    # Example: Europe region analysis  
    europe_balance = BalanceIndex(33.9, 15.5, region="Europe")
    print(f"Europe Balance Index: {europe_balance.calculate():.3f}")
    print(f"Europe Interpretation: {europe_balance.interpretation()}")
