class RecommendationEngine:
    def __init__(self):
        self.advice = {
            "Boron": {
                "fertilizer": "Borax or Solubor",
                "dosage": "10–15 kg/ha",
                "method": "Apply as soil amendment or foliar spray",
                "note": "Avoid overuse to prevent toxicity"
            },
            "Calcium": {
                "fertilizer": "Calcium Nitrate or Gypsum",
                "dosage": "200–300 kg/ha",
                "method": "Broadcast and incorporate into soil",
                "note": "Ensure proper soil pH for absorption"
            },
            "Iron": {
                "fertilizer": "Ferrous Sulfate or Chelated Iron (Fe-EDTA)",
                "dosage": "2–5 kg/ha",
                "method": "Foliar spray or soil drench",
                "note": "Apply during early morning for best uptake"
            },
            "Potassium": {
                "fertilizer": "Muriate of Potash (MOP)",
                "dosage": "100g per plant",
                "method": "Apply near root zone and mix with soil",
                "note": "Avoid overwatering after application"
            },
            "Magnesium": {
                "fertilizer": "Magnesium Sulfate (Epsom Salt)",
                "dosage": "25–50 kg/ha",
                "method": "Foliar spray or soil application",
                "note": "Combine with nitrogen for better uptake"
            },
            "Manganese": {
                "fertilizer": "Manganese Sulfate",
                "dosage": "5–10 kg/ha",
                "method": "Foliar spray or soil incorporation",
                "note": "Avoid mixing with phosphate fertilizers"
            },
            "Sulphur": {
                "fertilizer": "Elemental Sulphur or Ammonium Sulphate",
                "dosage": "20–40 kg/ha",
                "method": "Broadcast and mix into soil",
                "note": "Apply before rainy season for better absorption"
            },
            "Zinc": {
                "fertilizer": "Zinc Sulfate",
                "dosage": "10–25 kg/ha",
                "method": "Soil application or foliar spray",
                "note": "Use chelated forms in alkaline soils"
            },
            "Healthy": {
                "fertilizer": "None needed",
                "dosage": "N/A",
                "method": "N/A",
                "note": "Your plant is healthy!"
            }
        }

    def get_recommendation(self, deficiency_class):
        return self.advice.get(deficiency_class, {
            "fertilizer": "N/A",
            "dosage": "N/A",
            "method": "N/A",
            "note": "No recommendation available"
        })
