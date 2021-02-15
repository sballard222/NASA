module sorters
implicit none

contains

subroutine bubblesort(array,length)
real, dimension(length),intent(inout)   :: array
integer,                intent(in)      :: length

real                      :: temp
integer                   :: i,j,n

! Sorts a vector using bubble sort.  Returns sorted vector in place.
! Sorts in ascending order.

  do i=1,length
     do j=1,length
        if (array(i) .lt. array(j)) then
            temp = array(i)
            array(i) = array(j)
            array(j) = temp
        endif
     enddo
  enddo

return
end subroutine bubblesort

subroutine pbsort(x,perms,length)
real,    dimension(length), intent(inout) :: x
integer, dimension(length), intent(out)   :: perms
integer,                    intent(in)    :: length

real                        :: temp
integer                     :: itemp
integer                     :: i,j

! Sorts a vector with a simple bubble sort.  Returns sorted vector in place 
! along with the permutation vector.  Sorts in ascending order.

  do i=1,length
     perms(i)=i
  enddo

  do i=1,length
     do j=1,length
        if (x(i) .lt. x(j)) then
            temp  = x(i)
            itemp = perms(i)
            x(i) = x(j)
            perms(i)=perms(j)
            x(j) = temp
            perms(j)=itemp
        endif
     enddo
  enddo

return

end subroutine pbsort


subroutine shellsort(array,length)
real, dimension(length), intent(inout) :: array
integer,                 intent(in)    :: length

real                    :: temp
integer                 :: inc,lower,upper
integer                 :: i,j

! Sorts an array with indices running from 1 to length in place using Shell sort

lower=lbound(array,1)
upper=ubound(array,1)

inc=length/2

! We continue until the stride is the lower bound

do while (inc > 0)
   do i=inc+lower,upper
      temp=array(i)
      j=i
      do while ( j > inc .and. array(j-inc) > temp )
         array(j)=array(j-inc)
         j=j-inc
      enddo
      array(j)=temp
   enddo
   if ( inc == 2 ) then
      inc=1
   else
      inc=int(real(inc)/2.2)
   endif
enddo

end subroutine shellsort


subroutine pshellsort(array,perms,length)
real, dimension(length),  intent(inout) :: array
integer,dimension(length),intent(out)   :: perms
integer,                  intent(in)    :: length

real                    :: temp
integer                 :: itemp
integer                 :: inc,lower,upper
integer                 :: i,j

! Sorts an array with indices running from 1 to length in place using Shell sort

lower=lbound(array,1)
upper=ubound(array,1)

do i=1,length
   perms(i)=i
enddo

inc=length/2

! We continue until the stride is the lower bound

do while (inc > 0)
   do i=inc+lower,upper
      temp=array(i)
      itemp=perms(i)
      j=i
      ! This only works if the compiler short-circuits
      do while ( j > inc .and. array(j-inc) > temp )
         array(j)=array(j-inc)
         perms(j)=perms(j-inc)
         j=j-inc
      enddo
      array(j)=temp
      perms(j)=itemp
   enddo
   if ( inc == 2 ) then
      inc=1
   else
      inc=int(real(inc)/2.2)
   endif
enddo

end subroutine pshellsort


subroutine mergesort(array,length)
real, dimension(length), intent(inout) :: array
integer,                 intent(in)    :: length

real, allocatable, dimension(:) :: temp

! Local allocatable will be deallocated on exit from subroutine
   allocate(temp((length+1)/2))
   call m_sort(array,temp,length)

end subroutine mergesort

recursive subroutine m_sort(array,temp,length)
real, dimension(length),       intent(inout) :: array
integer,                       intent(in)    :: length
real, dimension((length+1)/2), intent(inout) :: temp

integer                       :: midpoint,righthalf
real                          :: swapper

    if ( length < 2 ) return
    if ( length .eq. 2 ) then
         if ( array(1) > array(2) ) then
              swapper=array(1)
              array(1)=array(2)
              array(2)=swapper
         endif
         return
    endif

    midpoint=(length+1)/2
    righthalf=length-midpoint

    call m_sort(array,temp,midpoint)
    call m_sort(array(midpoint+1),temp,righthalf)

    if ( array(midpoint) > array(midpoint+1) ) then
       temp(1:midpoint)=array(1:midpoint)
       call merger(array,temp,array(midpoint+1),length,midpoint,righthalf)
    endif

end subroutine m_sort

subroutine merger(array,array1,array2,length,l1,l2)
real, dimension(length), intent(inout) :: array
real, dimension(l1),     intent(inout) :: array1
real, dimension(l2),     intent(inout) :: array2
integer,                 intent(in)    :: length,l1,l2

integer                 :: i,j,k

   i=1; j=1; k=1

   do while ( ( i <= l1 ) .and. ( j <= l2 ))
      if ( array1(i) <= array2(j) ) then
           array(k)=array1(i)
           i=i+1
      else
           array(k)=array2(j)
           j=j+1
      endif
      k=k+1
   enddo

   do while (i <= l1)
      array(k)=array1(i)
      i=i+1
      k=k+1
   enddo

end subroutine merger

end module sorters
