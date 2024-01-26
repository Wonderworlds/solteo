## Exercise
When a customer wants to sell its solar-panel-produced electricity, the installer needs to fill a electricity netword connexion request to ENEDIS.

We are interested in displaying the ENEDIS records of this requests.

By modifying the `app/page.tsx` file, display these records in table. Mandatory fields to display:
* annee
* date (should be formatted to display a readable date)
* type_production
* type_injection
* mw

These records can be accessed at the open data API provided by Enedis (https://api.gouv.fr/documentation/api-donnees-ouvertes-enedis). The dataset we are interested is called : `Projets en développement - Sorties des demandes - Evolution`

We should be able to see how many records there are in total, and to select how many results we want to display.

Feel free to add custom search parameters.

You can add and use every lib you want.
## Getting Started

To run the development server:

```bash
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.
