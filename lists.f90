module lists
! This module specifies that list_type equates to whatever type is desired.
! If it is not a primitive type, the module that describes the type must 
! overload the assigment operator.  For example, for a type Cards we would have
!use Cards, list_type=>Card
! Author:    K. Holcomb, inspired by code by Arjen Markus
! Changelog: Initial version     2012-11-01
!            Added pop method    2013-03-06
!            Added insert method 2013-06-02
implicit none

   type(list_type)
       character  :: string
   end type 

   contains

   subroutine append(list,new_item)
   type(list_type), dimension(:), allocatable, intent(inout) :: list
   type(list_type),                            intent(in)    :: new_item
   type(list_type), dimension(:), allocatable                :: temp_list
   integer                                                   :: n, list_len

      if ( .not. allocated(list) ) then
          allocate(list(1))
          list(1)=new_item
      else
         list_len=size(list)
         allocate(temp_list(list_len))

         do n=1,list_len
            temp_list(n)=list(n)
         enddo

         deallocate(list)
         allocate(list(list_len+1))

         do n=1,list_len
            list(n)=temp_list(n)
         enddo
         list(list_len+1)=new_item

      endif

   end subroutine append


   subroutine insert(list,new_item,list_index)
   type(list_type), dimension(:), allocatable, intent(inout):: list
   type(list_type),                            intent(in)   :: new_item
   integer,                       optional,    intent(in)   :: list_index
   type(list_type), dimension(:), allocatable               :: temp_list
   integer                                                  :: before_index
   integer                                                  :: list_len
   integer                                                  :: n, ncount

      if ( present(list_index) ) then
          before_index=list_index
      else
          before_index=1
      endif

      list_len=size(list)
      if ( before_index > list_len ) then
          write(*,*) "List index not in range of list"
          return
      endif

      allocate(temp_list(list_len+1))

      if ( before_index>1) then
         do n=1,before_index-1
            temp_list(n)=list(n)
         enddo
      endif

      temp_list(before_index)=new_item

      do n=before_index,list_len
         temp_list(n+1)=list(n)
      enddo

      deallocate(list)
      allocate(list(list_len+1))
      do n=1,list_len+1
         list(n)=temp_list(n)
      enddo

   end subroutine insert


   subroutine delete(list,list_index)
   type(list_type), dimension(:), allocatable, intent(inout) :: list
   integer,                                    intent(in)    :: list_index
   type(list_type), dimension(:), allocatable                :: temp_list
   integer                                                   :: list_len
   integer                                                   :: n, ncount

      if ( .not. allocated(list) .or. size(list)<1 ) then
           write(*,*) "Empty list, cannot remove item"
          return
      endif

      list_len=size(list)

      if ( list_index > list_len ) then
           write(*,*) "List index not in range of list"
           return
      endif

      allocate(temp_list(list_len))

      do n=1,list_len
         temp_list(n)=list(n)
      enddo

      deallocate(list)
      allocate(list(list_len-1))

      ncount=1
      do n=1,list_len
         if ( n .ne. list_index ) then
            list(ncount)=temp_list(n)
            ncount=ncount+1
         endif
      enddo

   end subroutine delete


   function pop(list,list_index) result (pop_item)
   type(list_type)                                           :: pop_item
   type(list_type), dimension(:), allocatable, intent(inout) :: list
   integer,                       optional,    intent(in)    :: list_index
   integer                                                   :: pop_index
   integer                                                   :: list_len

       list_len=size(list)
 
       if (present(list_index)) then
           pop_index=list_index
       else
           pop_index=list_len
       endif

       pop_item=list(pop_index)
       call delete(list,pop_index)
   
   end function pop


   function is_in(list,test_item)
   logical                                                :: is_in
   type(list_type), dimension(:), intent(in)              :: list
   integer                                                :: nvals, n

      if ( size(list)<1 ) then
           write(*,*) "Empty list, cannot test item"
          return
      endif

      nvals=size(list)

      is_in=.false.
      do n=1,nvals
         if ( test_item==list(n) ) then
            is_in=.true.
            exit
         endif
      enddo     

   end function is_in

end module lists 
