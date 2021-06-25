-- sudoku

-- operations:
--  - display
--  - get constraints for i,j
--  - update i,j with x

-- data:
-- list of 81 tuples: (number, set of constraints)
-- sort fields by constraints: few constraints are handled first 
--  - sort list of fields, few options are looked at first
--  - among single-options, handle them in any order
--  - when single-options are done, resort the list
--  - if no single-options exist, we need smarter strats

import qualified Data.Vector as V


emptyLine :: V.Vector Int
emptyLine = V.replicate 10 0

type Sudoku = V.Vector (V.Vector Int)

emptySudoku :: Sudoku
emptySudoku = V.replicate 10 emptyLine

get :: Sudoku -> Int -> Int -> Int
get s x y = (s V.! x) V.! y

put :: Sudoku -> Int -> Int -> Int -> Sudoku
put s x y n = s V.// [(x, (s V.! x) V.// [(y, n)])]

getRow :: Sudoku -> Int -> [Int]
getRow s n = V.toList $ s V.! n
 
getCol :: Sudoku -> Int -> [Int]
getCol s n = [row V.! n | row <- V.toList s]
 


