module Main where

import Data.Function (on)
import Data.List (maximumBy)

isPalindrome :: String -> Bool
isPalindrome s =
  let reversed = reverse s
   in s == reversed

longestPali :: String -> String
longestPali s
  | isPalindrome s = s
  | length s == 2 = init s
  | otherwise =
      let leftReduction = longestPali $ tail s
          rightReduction = longestPali $ init s
          bothReduction = longestPali $ (init . tail) s
       in maximumBy (compare `on` length) [leftReduction, rightReduction, bothReduction]

main :: IO ()
main = do
  let cases = ["babad", "cbbd", "xabax", "abbcccbbbcaaccbababcbcabca"]
  let solutions = map longestPali cases
  print $ zip cases solutions
