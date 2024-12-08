(ns day8)

(defn parse_input [filename]
  (clojure.string/split (slurp filename) #"\n")
  )

(defn get-index [item coll]
  (remove nil?
          (map-indexed (fn [ix x] 
                         (let [i (clojure.string/index-of x item)]
                                    (when i [ix i])
                                    )
                         )
                       coll
                       )
          )
  )

(defn find_antenna_groups [input]
  (let [unique_antennas (filter (fn [x] (not= \. x)) (distinct (reduce str input)))]

  (->>
   (map (fn [antenna] {antenna (get-index antenna input)}) unique_antennas)
   (reduce merge {})
   )
  )
  )

(defn single_mapper [ant1 ant2]
  (let [x1 (first ant1)
        y1 (second ant1)
        x2 (first ant2)
        y2 (second ant2)
        xdiff (- x2 x1)
        ydiff (- y2 y1)
        ]
    [
     [(+ x1 (* 2 xdiff)) (+ y1 (* 2 ydiff))]
     [(- x2 (* 2 xdiff)) (- y2 (* 2 ydiff))]
     ]
    )
  )

(defn resonant_mapper [ant1 ant2 max_x max_y]
  (let [x1 (first ant1)
        y1 (second ant1)
        x2 (first ant2)
        y2 (second ant2)
        xdiff (- x2 x1)
        ydiff (- y2 y1)
        ]
    (def node1 (atom [x1 y1]))
    (def node2 (atom [x2 y2]))
    (def nodes (atom []))

    (while (and
            (<= 0 (first @node1) max_x)
            (<= 0 (second @node1) max_y)
            ) 
      (swap! nodes conj [(first @node1) (second @node1)])
      (swap! node1 
             (fn [node] [(+ (first node) xdiff) (+ (second node) ydiff)]) 
)
      )
    (while (and
            (<= 0 (first @node2) max_x)
            (<= 0 (second @node2) max_y)
            ) 
      (swap! nodes conj [(first @node2) (second @node2)])
      (swap! node2 
             (fn [node] [(- (first node) xdiff) (- (second node) ydiff)])
      )
    )
    @nodes
    ) 
  )

(defn find_antinodes [group max_x max_y mapper resonant?]
  (let [pairs (for [x group
                    y group
                    :when (not= x y)]
               [x y])
       ]
    (->> pairs
         (map (fn [[ant1 ant2]]
                (if resonant?
                  (mapper ant1 ant2 max_x max_y)
                  (mapper ant1 ant2)
                )
                )
              )
         (reduce concat)
         (distinct)
         (filter (fn [[x y]]
                   (and
                    (<= 0 x max_x)
                    (<= 0 y max_y)
                    )
                   )
                 )
         )
  )
)


(defn part1 [filename]
  (let [input (parse_input filename)
        max_x (dec (count (first input)))
        max_y (dec (count input))
        groups (find_antenna_groups input)
        ]
    (->> groups
         (vals)
         (map (fn [group] (find_antinodes group max_x max_y single_mapper false))) 
         (reduce concat)
         (distinct)
         (count)
         )
     )
  )

(defn part2 [filename]
  (let [input (parse_input filename)
        max_x (dec (count (first input)))
        max_y (dec (count input))
        groups (find_antenna_groups input)]
    (->> groups
         (vals)
         (map (fn [group] (find_antinodes group max_x max_y resonant_mapper true)))
         (reduce concat)
         (distinct)
         (count)
         )
    )
  )