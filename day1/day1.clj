(ns day1)

(defn parse_input [filename]
  (as-> filename input
  (clojure.string/split (slurp input) #"\n")
  (map (fn [x] (clojure.string/split x #"   ")) input)
  (map (fn [x] (map #(Integer/parseInt %) x)) input)
  (map (fn [x] (vec x)) input))
  )

(defn two_lists [input]
  (let [l1 (vec (map first input))
        l2 (vec (map second input))] 
    [(sort l1) (sort l2)]
    )
  )

(defn list_diff [[l1 l2]]
  (map (comp abs -) l1 l2)
  )

(defn single_score [digit list]
  (* digit (count (filter #(= digit %) list))))

(defn similarity_score [[list1 list2]]
  (reduce + (map #(single_score % list2) list1))
  )

(defn part1 [filename]
  (->> filename
       parse_input
       two_lists
       list_diff
       (reduce +)
       )
  )

(defn part2 [filename]
  (->> filename
       parse_input
       two_lists
       similarity_score
       )
  )

(part1 "day1/real_input1.txt")
(part2 "day1/real_input1.txt")