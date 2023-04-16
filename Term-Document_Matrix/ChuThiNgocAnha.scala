object Indexer{

    def build(inputPath: String, outputPath: String): Map[String, List[Int]] = {
        val files = Filed.list(Paths.get("D:/IR/Term-Document_Matrix/test")).collect(java.util.stream.Collectors.toList()).asScala.toList.map(_.getFileName().toString)
        val tokens = file.map { file =>
            val fileName = inputPath + '/' + file
            val ts = Source.fromFile(fileName, "iso-8859-1").getLines().toList.flatMap(line => line.split("""[\s,?]+"""))
            (file, ts)

        }
        val vocab = tokens.map(_._2).flatMap(identity).toSet.toList.sorted 
        val index = vocab.map {term =>
            val docIds = tokens.filter(_._2.contains(term)).map(_._1.toInt)
            (term, docIds)
        }.toMap
        val content = index.map { case (term, docIds)
            term + "\t" + docIds.mkString(" ")
        }.mkString("\n")
        files.writeString(Paths.get(outputPath), content)
        index
    }

    def load(indexPath: String): Map[String, List[Int]] = {
        ??? 

    }

    def main(args: Array[String]): Unit = {
        val index = build("D:/IR/Term-Document_Matrix/test", "index.txt")


    }

}







// crawling/scraping
// (Preprocessing)
// main content
// Tìm hiểu cách crawling
// python: trafilatura
// brew install trafilatura


// sbt new scala/scala-seed.g8 - taoj project mới trong thư mục hiện tại