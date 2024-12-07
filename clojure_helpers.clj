(ns helpers)

(defn parse_input_colon_separated [filename]
  (->> (slurp filename)
       (clojure.string/split-lines)
       (map (fn [line] (clojure.string/split line #": ")))
       (map
        (fn [line] [
                    (Long/parseLong (get line 0))
                    (map Integer/parseInt (clojure.string/split (get line 1) #" "))
                    ]
          )
        )
       )
  )

(defn cartesian_product [colls]
  (if (empty? colls)
    '(())
    (for [more (cartesian_product (rest colls))
          x (first colls)]
      (cons x more)
      )
    )
  )