object BooleanSearch{


    def search(index: Map[String, List[Int]], tom: String): List[Int]= {
        // if(index.contains(tom))
        //     index(tom)
        // else
        //     List.empty
        
        index.getOrElse(tom, List.empty)
    }

    def searchAnd(index: Map[String, List[Int]], tom: String, jerry: String): List[Int] = {
        val t = search(index, tom)
        val j = search(index, jerry)
        t.intersect(j)
    }

    def searchOr(index: Map[String, List[Int]], tom: String, jerry: String): List[Int] = {
        val t = search(index, tom)
        val j = search(index, jerry)
        (t ++ j).distinct
    }

    def andNot(index: Map[String, List[Int]], tom: String, jerry: String): List[Int] = {
        val t = search(index, tom)
        val j = search(index, jerry)
        t.diff(j)
    }

    def orNot(index: Map[String, List[Int]], tom: String, jerry: String): List[Int] = {
        val t = search(index, tom)
        val j = search(index, jerry)
        a = index.values.flatMap(identity).toList.distinct
        (t ++ a.diff(j)).distinct.sorted
    }

    def main(args: Array[String]): Unit = {
        val index = Map("tom" -> List(1, 4, 8, 10),
                        "jerry" -> List(1, 4, 7),
                        "dog" -> List(1, 7, 11, 13),
                        "cat" -> List(2, 4, 7)
        )
        println(search(index, "tom"))
        println(searchAnd(index, "tom", "jerry"))
        println(searchOr(index, "tom", "jerry"))
        println(andNot(index, "tom", "jerry"))
        println(orNot(index, "tom", "jerry"))

    }
}
