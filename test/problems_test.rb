require 'minitest/autorun'
require 'minitest/reporters'
require_relative '../lib/problems'

Minitest::Reporters.use! Minitest::Reporters::SpecReporter.new

describe "Test wave 3 problems" do
  describe "balanced" do
    it "Given balanced strings it should return true" do
      
      expect(balanced('(({}))')).must_equal true
    end

    it "regards an empty string as balanced" do
      
      expect(balanced('')).must_equal true
    end

    it "will return false for an unbalanced set of parens" do
      
      expect(balanced('(()')).must_equal false
      expect(balanced('(()}')).must_equal false
      expect(balanced('([]]')).must_equal false
    end

    it "also works for {} and []" do
      
      expect(balanced('[]')).must_equal true
      expect(balanced('{}')).must_equal true
    end

    it "also works if the string has opens and closes in the beginning and end" do
      
      expect(balanced('[]()')).must_equal true
    end
  end

  describe "postfix" do
    it "can add a 2 numbers together" do
      
      expect(evaluate_postfix("34+")).must_equal 7
      expect(evaluate_postfix("34*")).must_equal 12
      expect(evaluate_postfix("34-")).must_equal -1
      expect(evaluate_postfix("34/")).must_equal 0
    end

    it "can add a evaluate a more complicated expression" do
      
      expect(evaluate_postfix("34+2*")).must_equal 14
      expect(evaluate_postfix("34*2/")).must_equal 6
      expect(evaluate_postfix("34-1+")).must_equal 0
      expect(evaluate_postfix("34/7-")).must_equal -7
      expect(evaluate_postfix("35+6*")).must_equal 48
      expect(evaluate_postfix("62/5+")).must_equal 8
    end
  end
end