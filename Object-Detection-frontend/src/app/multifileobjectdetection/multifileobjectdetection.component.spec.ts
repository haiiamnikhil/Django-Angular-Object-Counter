import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MultifileobjectdetectionComponent } from './multifileobjectdetection.component';

describe('MultifileobjectdetectionComponent', () => {
  let component: MultifileobjectdetectionComponent;
  let fixture: ComponentFixture<MultifileobjectdetectionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MultifileobjectdetectionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MultifileobjectdetectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
