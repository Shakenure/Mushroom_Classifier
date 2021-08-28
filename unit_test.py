import unittest
import predictNB
import NaiveBayesClassifier

class Testapp(unittest.TestCase):

    def test_edibility(self):
        result=predictNB.edibility(0.27,0.73)
        self.assertEqual(result,"Poisonous")

    def test_ProbFactor(self):
        inputValues={'CapShape':'bell'}
        E = 1
        P = 1
        for attr, attrType in inputValues.items():
            E = E*predictNB.getP( NaiveBayesClassifier.freq,'P_X_Edible', attr, attrType)*10
            P = P*predictNB.getP(NaiveBayesClassifier.freq,'P_X_Poisonous', attr, attrType)*10
        result=predictNB.edibility(E, P)
        self.assertEqual(result,"Edible")

    
    def test_cb(self):
        result=NaiveBayesClassifier.conditional_Prob("CapShape")
        self.assertIsNotNone(result)
 

    def test_getpPositive(self):
        
        result=predictNB.getP(NaiveBayesClassifier.freq,'P_X_Edible','CapColor', 'green')
        self.assertGreaterEqual(result,0)
        
        
    def test_getpNegative(self):
        
        result=predictNB.getP(NaiveBayesClassifier.freq,'P_X_Edible','CapColor', 'green')
        self.assertLessEqual(result,1)
        
    def test_ColumnNo(self):
            self.assertEqual(len(NaiveBayesClassifier.X.columns),22)
     
    
if __name__ == '__main__':
    unittest.main()