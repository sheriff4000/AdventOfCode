(ns day7)
(require 'helpers)


(defn parse_ops [ops values]
  (reduce (fn [acc [op val]] (
                              case op
                                "+" (+ acc val)
                                "*" (* acc val) 
                                "||" (Long/parseLong (str acc val))
                              )
                              ) 
          (first values) 
          (map vector ops (rest values)) 
  )
)

(defn is_valid? [target values perms]
  (if (empty? perms)
    false
    (if (= target (parse_ops (first perms) values))
      true
      (recur target values (rest perms)))
    )
)

(defn check_valid [[target values operators]]
  (let 
   [
    permutations 
    (helpers/cartesian_product (repeat (- (count values) 1) operators))
    ]
    (is_valid? target values permutations)
  )
)

(defn solve [input ops]
  (reduce (fn [total [target values]] 
            (
             if (check_valid (conj [target values] ops)) 
             (+ total target)
             total
             ) 
            )
            0
          input
          )
  )

(defn get_answers [filename]
  (let [inputs 
        (helpers/parse_input_colon_separated filename)]
  (println (str "Part 1: " (solve inputs ["+" "*"])))
  (println (str "Part 2: " (solve inputs ["*" "+" "||"])))
  )
)

(get_answers "day7/real.txt")
