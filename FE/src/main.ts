import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { TemplateSitoComponent } from './app/template-sito/template-sito.component';

platformBrowserDynamic().bootstrapModule(TemplateSitoComponent, {
  ngZoneEventCoalescing: true
})
  .catch(err => console.error(err));
