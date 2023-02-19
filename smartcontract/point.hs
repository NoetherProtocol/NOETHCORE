data Coordinate = Point Int Int deriving Show

localidad :: Coordinate
localidad = Point 1 1

coordinateFunction :: Coordinate -> Coordinate
coordinateFunction(Point x y) = Point (x+y) (x-y)

main = do
print $ (coordinateFunction . coordinateFunction) localidad