import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TemplateSitoComponent } from './template-sito.component';

describe('TemplateSitoComponent', () => {
  let component: TemplateSitoComponent;
  let fixture: ComponentFixture<TemplateSitoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TemplateSitoComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TemplateSitoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
