{-# LANGUAGE OverloadedStrings #-}

module Main where

import Language.Marlowe
import Language.Marlowe.Client
import Data.Text (Text)

main :: IO ()
main = print . pretty $ contract

-- Participants
benjamin, hector :: Party
benjamin = Role "Benjamin"
hector = Role "Hector"

-- Token
ada :: Token
ada = Token "" ""

-- Contract
contract :: Contract
contract =
  When
    [ Case
        (Deposit benjamin benjamin ada 30)
        (Pay benjamin (Account hector) ada 30
          Close)
    ]
    30
    Close