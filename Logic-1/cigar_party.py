def cigar_party(cigars, is_weekend):
  if is_weekend == False:
    if cigars < 40 or cigars > 60:
      return False
    else:
      return True
  else:
    if cigars < 40:
      return False
    else:
      return True