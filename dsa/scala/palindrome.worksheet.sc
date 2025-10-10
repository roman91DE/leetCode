import scala.annotation.tailrec

object Solution1 {

  def isPalindrome(x: Int): Boolean = {

    @tailrec
    def is_pali1(s: String): Boolean =
      if s.head != s.last then false
      else if s.length <= 2 then true
      else is_pali1(s.slice(1, s.length - 1))

    is_pali1(x.toString())
  }
}

object Solution2 {
  def isPalindrome(x: Int): Boolean = {

    def helper(s: String): Boolean = s == s.reverse

    helper(x.toString())

  }
}

Solution1.isPalindrome(121)

object Solution3 {
  def isPalindrome(x: Int): Boolean = {

    def helper(s: String): Boolean = {
      val len = s.length
      len match
        case 0 | 1 => true
        case _ => {
          val (low, high) = s.splitAt(len/2)
          low.lazyZip(high.reverse).forall(_ == _)
        }
    }
    helper(x.toString())
  }
}



object Solution4 {
  def isPalindrome(x: Int): Boolean = {
    if (x < 0) return false
    val s = x.toString
    
    @tailrec
    def loop(lo: Int, hi: Int): Boolean =
      if (lo >= hi) true
      else if (s.charAt(lo) != s.charAt(hi)) false
      else loop(lo + 1, hi - 1)
    
    loop(0, s.length - 1)
  }
}


