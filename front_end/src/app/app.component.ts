import { Component, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  mainView = 'menu';

  onNavigate(feature: string) {
    this.mainView = feature;
  }
}
