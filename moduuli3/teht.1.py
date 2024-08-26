kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä:  "))
alamitta = 37

if kuhan_pituus < alamitta:
    puuttuva_mitta = alamitta - kuhan_pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin veteen!"
          f" Kuha on {puuttuva_mitta:.1f} cm liian lyhyt." )

