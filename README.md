# 🏆 ATP Tour Tennis - Intégration Home Assistant

![ATP Logo](./assets/icon.png)

Cette intégration Home Assistant vous permet de suivre le **classement ATP**, les **tournois en cours**, et les **matchs à venir** directement depuis votre tableau de bord.

## Installation via HACS

1. Ouvrez HACS dans Home Assistant.
2. Cliquez sur **Dépôts personnalisés**.
3. Ajoutez `https://github.com/SoFarSoGood86/ha-atp-tour` comme dépôt **Intégration**.
4. Installez “ATP Tour Tennis”.
5. Redémarrez Home Assistant.

## Configuration manuelle

```yaml
sensor:
  - platform: atp_tour
```

## Entités créées

- `sensor.novak_djokovic_atp_rank` → Classement + points
- `sensor.roland_garros_tournament` → Infos tournoi
