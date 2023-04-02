{-# LANGUAGE OverloadedStrings #-}

import Language.Marlowe.Extended

main :: IO ()
main = print . pretty $ myContract

myContract :: Contract
myContract =
  When
    [Case
      (Deposit
        (Role "me")
        (Role "you")
        (Token "" "")
        (Constant 15)
      )
      Close
    ]
    1680449148638
    Close