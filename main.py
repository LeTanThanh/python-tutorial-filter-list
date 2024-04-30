if __name__ == "__main__":
  # Introduction to Python filter() function

  scores = [70, 60, 80, 90, 50]
  print(scores)
  filtered_scores = []
  for score in scores:
    if score >= 70:
      filtered_scores.append(score)
  print(filtered_scores)

  """
  filter(fn, list)
  """
  scores = [70, 60, 80, 90, 50]
  print(scores)
  filtered_scores = list(filter(lambda score: score >= 70, scores))
  print(filtered_scores)

  countries = [
    ["China", 1394015977],
    ["United States", 329877505],
    ["India", 1326093247],
    ["Indonesia", 267026366],
    ["Bangladesh", 162650853],
    ["Pakistan", 233500636],
    ["Nigeria", 214028302],
    ["Brazil", 21171597],
    ["Russia", 141722205],
    ["Mexico", 128649565]
  ]
  print(countries)
  filtered_countries = list(filter(lambda country: country[1] > 300_000_000, countries))
  print(filtered_countries)
